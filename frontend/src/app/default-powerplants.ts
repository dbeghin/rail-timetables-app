import { Powerplant } from './productionplan/payload.model';

export const POWERPLANTS_TRICKY: Powerplant[] = [
  {
    "name": "gasnormal",
    "type": "gas",
    "efficiency": 0.37,
    "pmin": 235,
    "pmax": 245
  },
  {
    "name": "gasannoying",
    "type": "gas",
    "efficiency": 0.33,
    "pmin": 25,
    "pmax": 30
  },
  {
    "name": "gasannoying2",
    "type": "gas",
    "efficiency": 0.33,
    "pmin": 25,
    "pmax": 30
  },
  {
    "name": "gasannoying3",
    "type": "gas",
    "efficiency": 0.33,
    "pmin": 25,
    "pmax": 30
  },
  {
    "name": "kero1",
    "type": "kerosine",
    "efficiency": 0.3,
    "pmin": 300,
    "pmax": 1600
  },
  {
    "name": "wind1",
    "type": "wind",
    "efficiency": 1,
    "pmin": 0,
    "pmax": 90
  },
  {
    "name": "wind2",
    "type": "wind",
    "efficiency": 1,
    "pmin": 0,
    "pmax": 21.6
  }
];


export const POWERPLANTS_SIMPLE: Powerplant[] = [
  {
    "name": "gasbig1",
    "type": "gas",
    "efficiency": 0.53,
    "pmin": 100,
    "pmax": 460
  },
  {
    "name": "gasbig2",
    "type": "gas",
    "efficiency": 0.53,
    "pmin": 100,
    "pmax": 460
  },
  {
    "name": "gassmaller",
    "type": "gas",
    "efficiency": 0.37,
    "pmin": 40,
    "pmax": 210
  },
  {
    "name": "kero1",
    "type": "kerosine",
    "efficiency": 0.3,
    "pmin": 0,
    "pmax": 16
  },
  {
    "name": "wind1",
    "type": "wind",
    "efficiency": 1,
    "pmin": 0,
    "pmax": 150
  },
  {
    "name": "wind2",
    "type": "wind",
    "efficiency": 1,
    "pmin": 0,
    "pmax": 36
  }
]