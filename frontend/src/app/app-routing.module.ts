import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UsersComponent } from './users/users.component';
import { ConnectionComponent } from './connection/connection.component';
import { ProductionplanComponent } from './productionplan/productionplan.component';

const routes: Routes = [
  { path: 'user', component: UsersComponent },
  { path: 'connection', component: ConnectionComponent },
  { path: 'productionplan', component: ProductionplanComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
