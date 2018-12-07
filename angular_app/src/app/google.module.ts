import {MatInputModule, MatProgressSpinnerModule, MatCardModule, MatToolbarModule ,MatMenuModule, MatRadioModule, MatButtonModule, MatIconModule, MatTabsModule, MatButtonToggleModule} from '@angular/material';
import { NgModule } from '@angular/core';

@NgModule({
  imports: [
    MatToolbarModule,
    MatInputModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatMenuModule,
    MatIconModule,
    MatRadioModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatTabsModule
    ],
  exports: [
    MatToolbarModule,
    MatProgressSpinnerModule,
    MatIconModule,
    MatInputModule,
    MatCardModule,
    MatMenuModule,
    MatRadioModule,
    MatButtonModule,  
    MatButtonToggleModule,
    MatTabsModule
    ],
})
export class GoogleModule { }