import { Component, OnInit,AfterViewInit, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { Observable, of } from 'rxjs';
import { MatTabChangeEvent } from '@angular/material';
import {NgxAutoScrollModule} from "ngx-auto-scroll";

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
      console.log(this.list)      
    })
  }
  ngAfterViewInit(){
  }


  // TODO Need to finish this method
  postLyrics() {
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

  postLyricsLocal(){
    console.log("postLyricsLocal")
    this.current_data ="haaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\n\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\n\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\n\nhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n" 
    setTimeout(function () {
      window.scrollTo(0, document.body.scrollHeight || document.documentElement.scrollHeight);
    }, 10);
  
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
      console.error(error); // log to console instead
      this.log(`${operation} failed: ${error.message}`);
      return of(result as T);
    };
  }
}