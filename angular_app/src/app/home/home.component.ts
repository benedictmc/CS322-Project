import { Component, OnInit } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { HttpClient } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  list: string[]

  results: Boolean = false
  artistFocus: string = ''

  
  constructor(private http: HttpClient) { }

  ngOnInit() {
    console.log("Loading page...")
    this.getArtists().subscribe(data=>{
      this.list = data
      console.log(this.list)      
    })
    this.getSamples('kanye').subscribe(data=>{
      console.log("Samples retruned are: ")      
      console.log(data)      
    })
  }
  // TODO Need to finish this method
  postLyrics(artist, body) {
    body = "hello"
    let url = 'http://localhost:5000/API/post-artists'
    return this.http.post(url, body).pipe(
      tap(_ => _),
      catchError(this.handleError('getArtists', []))
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