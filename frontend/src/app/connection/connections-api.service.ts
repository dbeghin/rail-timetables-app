import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {catchError, map, tap } from 'rxjs/operators';
import {API_URL} from '../env';
import {Connection} from './connection.model';
import { MessageService } from '../message.service';

const token = 'token';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json',
    Authorization: `Bearer ${token}`
  })
};


@Injectable({
  providedIn: 'root',
})
export class ConnectionsApiService {
  connectionsUrl = `${API_URL}/connection/`;
  constructor(
    private http: HttpClient,
    private messageService: MessageService,
  ) {   }

  private log(message: string) {
    this.messageService.add(`ConnectionsApiService: ${message}`);
  }

  // getUsers(): Observable<User[]> {
  //   const users = of(USERS);
  //   this.messageService.add('UsersApiService: fetched users');
  //   return users;
  // }

  getConnections(): Observable<Connection[]> {
    return this.http.get<Connection[]>(this.connectionsUrl/*, httpOptions*/)
      .pipe(
        tap(_ => this.log('fetched connections')),
        catchError(this.handleError<Connection[]>('getConnections', []))
      )
  }

  /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

     // TODO: send the error to remote logging infrastructure
     console.error(error); // log to console instead

     // TODO: better job of transforming error for user consumption
     this.log(`${operation} failed: ${error.message}`);

     // Let the app keep running by returning an empty result.
     return of(result as T);
    };
  }
}