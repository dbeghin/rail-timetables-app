import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable, of} from 'rxjs';
import {catchError, map, tap } from 'rxjs/operators';
import {API_URL} from '../env';
import {User} from './user.model';
//import { USERS } from '../mock-users';
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
export class UsersApiService {
  usersUrl = `${API_URL}/user/`;
  constructor(
    private http: HttpClient,
    private messageService: MessageService,
  ) {   }

  private log(message: string) {
    this.messageService.add(`UsersApiService: ${message}`);
  }


  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(this.usersUrl, httpOptions)
      .pipe(
        tap(_ => this.log('fetched users')),
        catchError(this.handleError<User[]>('getUsers', []))
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