import { Component } from '@angular/core';

@Component({
  templateUrl: 'bookkeepingaccounts.component.html',
  styleUrls: [ './bookkeepingaccounts.component.scss' ]
})

export class BookkeepingAccountsComponent {
  employee: any;
  employee2: any;
  colCountByScreen: object;

  constructor() {
    this.employee = {
      Number: 1,
      Description: 'Sales tax free',
      Group: '',
      VAT_Percent: '0',
      Picture: 'images/employees/06.png',
      Creation_date: new Date('1974/11/5'),
      Last_modified: new Date('2005/05/11'),
      /* tslint:disable-next-line:max-line-length */
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
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit2() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit3() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit4() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }

  onSubmit5() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit6() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit7() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSubmit8() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onNew() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onDelete() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSearch() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onUndo() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onSave() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onFirstPage() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onPreviousPage() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onNextPage() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onLastPage() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
  onExportData() {
    console.log("Form submitted!", this.employee);
    alert("Form submitted successfully!");
  }
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
