import { Component } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { AppService } from './services/shared.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'my-app';
  text:any;
  output: any;

  ReadMore:boolean = true;  
  visible:boolean = false;

  constructor(private sharedService: AppService , private http: HttpClient) { }

  getResult() {
    console.log(this.text);
    let ourElement = {text: this.text};
    this.sharedService.doSentimentAnalysis(ourElement).subscribe(
      res => {
        console.log('data: ', res);
        this.output = {...res};
        this.visible = true;
      }, 
      )
  }
  
}
