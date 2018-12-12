import { Component, OnInit } from '@angular/core';
import {Howl, Howler} from 'howler';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

  constructor() { }

  ngOnInit() {
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
      sound2.play()

  }

}
