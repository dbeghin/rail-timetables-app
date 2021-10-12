export class Fuels {
    public gas: number;
    public kerosine: number;
    public co2: number;
    public wind: number=0;
    constructor() {
        this.gas=10;
        this.kerosine=20;
        this.co2=0;
        this.wind=60;
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
        this.pmax=0;
    }
}

export class Payload {
    public load: number;
    public fuels: Fuels;
    public powerplants: Powerplant[];
    constructor() {
        this.load=200;
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