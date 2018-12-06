import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GoogleModule } from './google.module';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { HttpClientModule } from '@angular/common/http';
import { NavComponent } from './nav/nav.component';
import { SplashComponent } from './splash/splash.component';

const appRoutes: Routes = [
  { path: '', component: SplashComponent },
  { path: 'home', component: HomeComponent },

  ];


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NavComponent,
    SplashComponent
  ],
  imports: [
    BrowserModule,
    GoogleModule,
    AppRoutingModule,
    RouterModule.forRoot(
      appRoutes
    ),
    HttpClientModule,
    BrowserAnimationsModule 
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
