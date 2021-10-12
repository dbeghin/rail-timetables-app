import { Component, OnInit } from '@angular/core';

import { Connection } from './connection.model';
import { ConnectionsApiService } from './connections-api.service';

@Component({
  selector: 'app-connection',
  templateUrl: './connection.component.html',
  providers: [ConnectionsApiService],
  styleUrls: ['./connection.component.css']
})
export class ConnectionComponent implements OnInit {

  connections: Connection[] = [];

  constructor(private connectionsService: ConnectionsApiService) {}

  ngOnInit() {
    this.getConnections();
  }

  getConnections(): void {
    this.connectionsService.getConnections()
        .subscribe(connections => this.connections = connections);
  }


}
