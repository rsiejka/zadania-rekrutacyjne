import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { from } from 'rxjs';
import { filter, map, mergeMap, toArray } from 'rxjs/operators';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'reactivejs';

  agesArray: number[] = [];
  avgAgeFromPoland: number = 0;
  constructor(){

  let persons = [
    {
        id: 1,
        name: "Jan Kowalski"
    }, {
        id: 2,
        name: "John Doe"
    }, {
        id: 3,
        name: "Jarek Kaczka"
    }
  ]
    
  let ages = [
    {
        person: 1,
        age: 18
    }, {
        person: 2,
        age: 24
    }, {
        person: 3,
        age: 666
    }
  ]
    
  let locations = [
    {
        person: 1,
        country: "Poland"
    }, {
        person: 3,
        country: "Poland"
    }, {
        person: 1,
        country: "USA"
    }
  ]


  const ageStream$ = from(ages);
  const locationStream$ = from(locations);

  from(locations)
  .pipe(
    filter(location => location.country === 'Poland'),
    mergeMap(location =>
      from(ages).pipe(
        filter(age => age.person === location.person), 
        map(age => age.age)
      )
    ),
    toArray(),map(agesArray => {
      const total = agesArray.reduce((sum, age) => sum + age, 0);
      const average = total / agesArray.length;
      return {average};
    })
  )
  .subscribe(result => 
    this.avgAgeFromPoland = result.average);
  };

}
