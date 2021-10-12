export interface Id {
  $oid: string;
}

export interface Connection {
  _id: Id;
  connection_id: number;
  node_from: string;
  node_to: string;
}