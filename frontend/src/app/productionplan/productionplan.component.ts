import { Component, OnInit } from '@angular/core';
import { ProductionPlanApiService } from './productionplan-api.service';
import { Payload, Powerplant, OptimiserOutput } from './payload.model';
import { POWERPLANTS_TRICKY, POWERPLANTS_SIMPLE } from '../default-powerplants';

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
  iCounter : number = 0;

  constructor(private productionPlanApiService:ProductionPlanApiService) { }

  ngOnInit(): void {
  }

  onSelect(powerplant: Powerplant): void {
    this.selectedPowerplant = powerplant;
  }

  loadSimple() {
    this.powerplants = POWERPLANTS_SIMPLE;
    this.iCounter = 6;
  }

  loadTricky() {
    this.powerplants = POWERPLANTS_TRICKY;
    this.iCounter = 7;
  }

  clearPowerplants() {
    this.powerplants = [];
    this.iCounter = 0;
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
