import { Component, OnInit,AfterViewInit, ViewChild } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { MatTabChangeEvent } from '@angular/material';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  list: string[]
  arrayName: string
  map = new Map<string, string>(); 
  results: Boolean = false
  artistFocus: string = ''
  sampleFocus: string = ''
  kanyeSamples: Array<string> = ["I feel blessed Way up, I feel blessed nWay up, I feel blessed", 
  "I hate the new Kanye, the bad mood Kanye The always rude Kanye, spaz in the news Kanye",
  "When was the last time I remembered a birthday? When was the last time I wasn't in a hurry?"]
  beatlesSamples: Array<string> = ["It Won't Be Long,All I've Got To Do,All My Loving,Don't Bother Me",
  "Within You Without You,When I'm Sixty Four,Lovely Rita",
  "You Know What To Do,No Reply, Mr. Moonlight,Leave My Kitten Alone,Eight Days A Week"]
  loaded: string = '';
  current_data: string;

  constructor(private http: HttpClient) { }
  
  ngOnInit() {
    this.map.set("Kanye West", "this.kanyeSamples");
    this.map.set("The Beatles", "this.beatlesSamples");
    console.log("Loading page...")
    this.getArtists().subscribe(data=>{
      this.list = data
      console.log(this.list)      
    })
  }

  // TODO Need to finish this method
  postLyrics() {
    this.loaded = 'loading'
    let sample = this.sampleFocus
    let artist = this.artistFocus
    console.log('Generate button clicked with artist and sample', this.sampleFocus, sample)
    // {
    //   "artist" : artist,
    //   "sample" : sample
    // }
    let url = 'http://localhost:5000/API/post-artists'
    this.http.post('http://localhost:5000/API/post-artists', {
        "artist" : artist,
        "sample" : sample
      }).subscribe(
      data => {
          console.log("POST Request is successful ", data);
          this.current_data = data['result']
          this.loaded = 'done'
      },
      error => {
          console.log("Error", error);
      }
    );     
    console.log("Posting lyrics....")
  }

  getArtists (): Observable<any[]> {
    let url = 'http://localhost:5000/API/artists'
    return this.http.get<any[]>(url)
      .pipe(
        tap(_ => _),
        catchError(this.handleError('getArtists', []))
      );
  }
  tabChanged = (tabChangeEvent: MatTabChangeEvent, artistFocus: string): void => {
    let arrayName = eval(this.map.get(artistFocus));  
    console.log('index => ', tabChangeEvent.index);
    console.log('artist => ', artistFocus);
    console.log('text => ', arrayName[tabChangeEvent.index]);
    this.sampleFocus = arrayName[tabChangeEvent.index]
  }

  getSamples (id): Observable<any[]> {
    let url = 'http://localhost:5000/API/samples/'+id
    return this.http.get<any[]>(url)
      .pipe(
        tap(_ => _),
        catchError(this.handleError('getArtists', []))
      );
  }

  private log(message: string) {
    console.log(message);
  }

  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
   
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
   
      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);
   
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
}