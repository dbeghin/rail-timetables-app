export class Fuels {
    public gas: number;
    public kerosine: number;
    public co2: number;
    public wind: number;
    constructor() {
        this.gas=13.4;
        this.kerosine=133.5;
        this.co2=0;
        this.wind=100;
    }
}

export class Powerplant {
    public name: string;
    public type: string;
    public efficiency: number;
    public pmin: number;
    public pmax: number;
    constructor() {
        this.name ="powerplant name";
        this.type="default";
        this.efficiency=0.5;
        this.pmin=0;
        this.pmax=100;
    }
}

export class Payload {
    public load: number;
    public fuels: Fuels;
    public powerplants: Powerplant[];
    constructor() {
        this.load=721;
        this.fuels= new Fuels();
        this.powerplants= [new Powerplant()];
     }
}

export class OptimiserOutput {
    constructor(
        public msg: string,
        public powerplantsolutions: PowerplantSolution[],
    ) { }
}

export class PowerplantSolution {
    constructor(
        public name: string,
        public p: number,
    ) { }
}