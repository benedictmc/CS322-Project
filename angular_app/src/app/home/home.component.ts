import { Component, OnInit,AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { MatTabChangeEvent } from '@angular/material';
import {NgxAutoScrollModule} from "ngx-auto-scroll";
import {Howl, Howler} from 'howler';


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
  lyricError: Boolean = false
  loaded: string = '';
  current_data: string;

  constructor(private http: HttpClient, private scroll: NgxAutoScrollModule) { }
  
  ngOnInit() {
    this.map.set("Kanye West", "this.kanyeSamples");
    this.map.set("The Beatles", "this.beatlesSamples");
    console.log("Loading page...")
    this.getArtists().subscribe(data=>{
      this.list = data
    })
  }
  ngAfterViewInit(){
  }

  changeArtist(artist, event, kanye){
    this.artistFocus = artist
  }

  postLyrics() {
    this.current_data = " "
    this.loaded = 'loading'
    let sample = this.sampleFocus
    let artist = this.artistFocus
    console.log('Generate button clicked with artist and sample', this.sampleFocus, sample)

    let url = 'http://localhost:5000/API/post-artists'
    this.http.post('http://localhost:5000/API/post-artists', {
        "artist" : artist,
        "sample" : sample
      }).subscribe(
      data => {
          console.log("POST Request is successful ", data);
          this.current_data = data['result']
          setTimeout(function () {
            window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
          }, 10);
          console.log(this.current_data);
          this.loaded = 'done'
      },
      error => {
          console.log("Error", error);
          this.loaded = 'done'
          this.lyricError = true;
      }
    );     
    console.log("Posting lyrics....")
  }

  getArtists (): Observable<any[]> {
    let url = 'http://localhost:5000/API/artists'
    let testUrl = 'https://obscure-basin-64790.herokuapp.com/API/artists'
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
      console.error(error); // log to console instead
      this.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }


  playSound(){
    console.log("Button Clicked!")

    let sound1 = new Howl({
      src: ['../../assets/sound/adele.mp3']
    });
    let sound2 = new Howl({
      src: ['../../assets/sound/adele-background.mp3']
    });
      sound1.play()
      sound2.volume(0.35)
      sound2.play()

  }
}