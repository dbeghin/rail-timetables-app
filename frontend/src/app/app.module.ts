import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { FormsModule } from '@angular/forms'

import {AppComponent} from './app.component';
import {UsersApiService} from './users/users-api.service';
import { UsersComponent } from './users/users.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './app-routing.module';
import { ConnectionComponent } from './connection/connection.component';
import { ConnectionsApiService } from './connection/connections-api.service';
import { ProductionplanComponent } from './productionplan/productionplan.component';
import { PowerplantDetailComponent } from './powerplant-detail/powerplant-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    MessagesComponent,
    ConnectionComponent,
    ProductionplanComponent,
    PowerplantDetailComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
  ],
  providers: [
    UsersApiService,
    ConnectionsApiService
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}