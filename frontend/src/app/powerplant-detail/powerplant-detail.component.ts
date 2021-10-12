import { Component, OnInit, Input } from '@angular/core';
import { Powerplant } from '../productionplan/payload.model';

@Component({
  selector: 'app-powerplant-detail',
  templateUrl: './powerplant-detail.component.html',
  styleUrls: ['./powerplant-detail.component.css']
})

export class PowerplantDetailComponent implements OnInit {
  @Input() powerplant?: Powerplant;

  constructor() { }

  ngOnInit(): void {
  }

}
