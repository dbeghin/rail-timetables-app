import { Component, OnInit } from '@angular/core';
import { ProductionPlanApiService } from './productionplan-api.service';
import { Payload, Powerplant, OptimiserOutput } from './payload.model';
import { POWERPLANTS_DEFAULT } from '../default-powerplants';

@Component({
  selector: 'app-productionplan',
  templateUrl: './productionplan.component.html',
  styleUrls: ['./productionplan.component.css']
})

export class ProductionplanComponent implements OnInit {
  title = 'Production plan from payload';
  selectedPowerplant?: Powerplant;
  powerplants:Powerplant[] = POWERPLANTS_DEFAULT;
  optimiseroutput?:OptimiserOutput;
  payload = new Payload();
  iCounter : number = 0;

  constructor(private productionPlanApiService:ProductionPlanApiService) { }

  ngOnInit(): void {
  }

  onSelect(powerplant: Powerplant): void {
    this.selectedPowerplant = powerplant;
  }

  addPowerplant(type: string) {
    const newPP = new Powerplant();
    newPP.type = type;
    newPP.name = type+String(this.iCounter);
    if (type == 'wind') newPP.efficiency = 1;
    this.iCounter += 1;
    this.powerplants.push(newPP)
  }

  savePowerplant() {
    this.selectedPowerplant = undefined
  }

  deletePowerplant(powerplant: Powerplant) {
    const index: number = this.powerplants.indexOf(powerplant);
    this.selectedPowerplant = undefined;
    this.powerplants.splice(index, 1);
  }

  getProductionPlan() {
    this.payload.powerplants = this.powerplants;
    this.productionPlanApiService.getProductionPlan(this.payload)
      .subscribe(
        optimiseroutput => this.optimiseroutput = optimiseroutput
        );      
  }
}
