import { Component, OnInit } from '@angular/core';
import { ProductionPlanApiService } from './productionplan-api.service';
import { Payload, Powerplant, OptimiserOutput } from './payload.model';

@Component({
  selector: 'app-productionplan',
  templateUrl: './productionplan.component.html',
  styleUrls: ['./productionplan.component.css']
})

export class ProductionplanComponent implements OnInit {
  title = 'Production plan from payload';
  selectedPowerplant?: Powerplant;
  powerplants:Powerplant[] = [];
  optimiseroutput?:OptimiserOutput;
  payload = new Payload();

  constructor(private productionPlanApiService:ProductionPlanApiService) { }

  ngOnInit(): void {
  }

  onSelect(powerplant: Powerplant): void {
    this.selectedPowerplant = powerplant;
  }

  addPowerplant() {
    this.powerplants.push(new Powerplant())
  }

  savePowerplant() {
    this.selectedPowerplant = undefined
  }

  getProductionPlan() {
    this.payload.powerplants = this.powerplants;
    this.productionPlanApiService.getProductionPlan(this.payload)
      .subscribe(
        optimiseroutput => this.optimiseroutput = optimiseroutput
        );      
  }
}
