export class Access {
  constructor(
    public user: boolean = true,
    public admin: boolean = false,
  ) { }
}


export class User {
  constructor(
    //public _id: number = 1,
    public nym: string,
    public password: string,
    public access: Access = new Access(),
  ) { }
}