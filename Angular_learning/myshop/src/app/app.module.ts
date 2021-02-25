import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeadersComponent } from './headers/headers/headers.component';
import { LoginComponent } from './users/login/login.component';
import { RegisterComponent } from './users/register/register.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadersComponent,
    LoginComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
