import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  pokemons: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<any>('https://pokeapi.co/api/v2/pokemon?limit=1500').subscribe(
      (data) => {
        this.pokemons = data.results;
      }
    );
  }

  detailsAbilities : any[] = [];
  detailsForms : any[] = [];
  detailsVisible = 0
  detailName = '';

  showDetails(name: string,url: string){

    if(this.detailsVisible == 0){

    this.detailName = name;
    this.http.get<any>(url).subscribe(
      (data2) => {
        this.detailsAbilities = data2.abilities;
        this.detailsForms = data2.forms;
      }
    )
    this.detailsVisible = 1

    }else if (this.detailsVisible == 1 && this.detailName != name){

      this.detailName = name;
      this.http.get<any>(url).subscribe(
        (data2) => {
         this.detailsAbilities = data2.abilities;
         this.detailsForms = data2.forms;
        }
      )


    }else{

      this.detailsVisible = 0;
      this.detailsAbilities = [];
      this.detailsForms = [];
      this.detailName = '';
    }

  }
  }