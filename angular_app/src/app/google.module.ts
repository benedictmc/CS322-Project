import { MatToolbarModule ,MatMenuModule, MatRadioModule, MatButtonModule, MatIconModule, MatTabsModule, MatButtonToggleModule} from '@angular/material';
import { NgModule } from '@angular/core';

@NgModule({
  imports: [
    MatToolbarModule,
    MatMenuModule,
    MatIconModule,
    MatRadioModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatTabsModule
    ],
  exports: [
    MatToolbarModule,
    MatIconModule,
    MatMenuModule,
    MatRadioModule,
    MatButtonModule,  
    MatButtonToggleModule,
    MatTabsModule
    ],
})
export class GoogleModule { }