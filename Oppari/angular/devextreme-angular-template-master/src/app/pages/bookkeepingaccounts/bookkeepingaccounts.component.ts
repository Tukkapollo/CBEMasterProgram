import { Component } from '@angular/core';
import { ApiService } from 'src/app/shared/services/api.service';
import { lastValueFrom } from 'rxjs';
import { HttpErrorResponse } from '@angular/common/http';


@Component({
  templateUrl: 'bookkeepingaccounts.component.html',
  styleUrls: [ './bookkeepingaccounts.component.scss' ]
})
export class BookkeepingAccountsComponent {
  bookkeep: any;
  bookkeep2: any;
  colCountByScreen: object;
  successMessage: string = '';

  constructor(private apiService: ApiService) {
    this.bookkeep = {
      Number: 1,
      Description: 'Sales tax free',
      Group: '',
      VAT_Percent: '0',
      Creation_date: new Date('2024/10/14'),
      Last_modified: new Date('2024/11/24'),
      Notes: '',
      Cent_rounding: false
      
    };
    this.colCountByScreen = {
      xs: 0,
      sm: 2,
      md: 10,
      lg: 4
    };
  }
  onSubmit1() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit2() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit3() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit4() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }

  onSubmit5() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit6() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit7() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSubmit8() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onNew() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onDelete() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onSearch() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onUndo() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  async onSave() {
    try {
      const requestPayload = { 
        accountGroup: this.bookkeep.Group,   
        code: String(this.bookkeep.Number),
        creationDate: this.formatDate(new Date(this.bookkeep.Creation_date)), 
        description: this.bookkeep.Description,
        modifyDate: this.formatDate(new Date(this.bookkeep.Last_modified)), 
        template: false
      };

      const response = await lastValueFrom(this.apiService.put('BookkeepingAccount', requestPayload));
      this.successMessage = response.message;

    } catch (error:unknown) {
      let errorMessage = 'An unexpected error occurred.';

      if (error instanceof HttpErrorResponse) {
        if (typeof error.error == 'string') {
          this.successMessage = error.error; 
        } else if (error.error?.message) {
          this.successMessage = error.error.message; 
        } else {
          this.successMessage =`HTTP Error: ${error.status} - ${error.statusText}`;
        }
      } else if (error instanceof Error) {
        this.successMessage = error.message;
      }
    }
    setTimeout(() => {
      this.successMessage = '';
    }, 3000);
  }
  onFirstPage() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onPreviousPage() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onNextPage() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onLastPage() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  onExportData() {
    console.log("Form submitted!", this.bookkeep);
    alert("Form submitted successfully!");
  }
  formatDate = (date: Date) => {
    const day = ('0' + date.getDate()).slice(-2); // Get day and pad with leading zero
    const month = ('0' + (date.getMonth() + 1)).slice(-2); // Get month and pad with leading zero
    const year = date.getFullYear(); // Get year
  
    return parseInt(`${day}${month}${year}`); // Return formatted date in ddMMyyyy format
  };
  items = [
    { id: 3000, description: 'Sales Vat 25,5%' },
    { id: 3001, description: 'Sales Vat 14%' },
    { id: 3002, description: 'Sales Vat 10%' },
    { id: 3003, description: 'Sales tax free' }
  ];
  dropdownItems = [
    { id: 1, name: 'Any part of field' },
    { id: 2, name: 'Option Two' },
    { id: 3, name: 'Option Three' }
  ];
  
  selectedItem: number | null = null;
}
