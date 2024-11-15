import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CarItem } from '../shared/models/carItem';
import { FormsModule } from '@angular/forms';
import { LocalStorageService } from '../shared/local-storage.service';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule], 
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'

  
})


export class AppComponent {

  items : CarItem[]= [];

  constructor(private localStorageService: LocalStorageService) {
    var keys = Object.keys(localStorage),
    i = 0, key;
  
    for (; key = keys[i]; i++) {
      const val = this.localStorageService.getItem(key)
      this.items.push(new CarItem(key, val ? JSON.parse(val) : null));
    }
  }

  newCarName = '';
  newCarPart = '';
  newCarPrice = '';
  title = 'cars';

  addNewCar(){

    
      if(this.localStorageService.getItem(this.newCarName)){
          const item = (this.localStorageService.getItem(this.newCarName))
          var handle = item ? JSON.parse(item) : []
          this.localStorageService.removeItem(this.newCarName)
          handle.push([this.newCarPart, Number(this.newCarPrice)])
          this.items.push(new CarItem(this.newCarName, handle))
          this.localStorageService.setItem(this.newCarName, JSON.stringify(handle))
          window.location.reload();
      }else{
          this.items.push(new CarItem(this.newCarName, [[this.newCarPart, Number(this.newCarPrice)]]))
          this.localStorageService.setItem(this.newCarName, JSON.stringify([[this.newCarPart, Number(this.newCarPrice)]]))
      }
     
      this.newCarName = '';
      this.newCarPart = '';
      this.newCarPrice = '';

  }

  services: [string, number][] = [];
  servicesVisible = 0;
  serviceVisibleName = '';
  
  showServices(carName: string){

    if(this.servicesVisible == 0){
      for (var i = 0; i < this.items.length; i++){
        if (this.items[i].carName == carName){
          this.services = this.items[i].service;
          this.servicesVisible = 1;
          this.serviceVisibleName = carName;
          break;
        }
      }
    }else if (this.servicesVisible == 1 && this.serviceVisibleName != carName){
      for (var i = 0; i < this.items.length; i++){
        if (this.items[i].carName == carName){
          this.services = this.items[i].service;
          this.servicesVisible = 1;
          this.serviceVisibleName = carName;
          break;
        }
      }
    }else{
      this.services = [];
      this.serviceVisibleName = '';
      this.servicesVisible = 0;
    }
  } 

   }

