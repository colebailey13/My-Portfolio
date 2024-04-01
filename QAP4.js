js
let customer = {
  name: "Cole Bailey",
  birthDate: "2003-06-24",
  gender: "Male",
  roomPreferences: ["Jacuzzi", "King bed"],
  paymentMethod: "Credit card",
  mailingAddress: {
    street: "123 Main St",
    city: "ST. John's",
    state: "NL",
    zip: "A1A1A1"
  },
  phoneNumber: "555-555-5555",
  checkInDate: "2024-04-01",
  checkOutDate: "2024-04-07",
  calculateAge: function() {
    let today = new Date();
    let birthDate = new Date(this.birthDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    let month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  },
  calculateStayDuration: function() {
    let checkInDate = new Date(this.checkInDate);
    let checkOutDate = new Date(this.checkOutDate);
    let duration = (checkOutDate - checkInDate) / (1000 * 60 * 60 * 24);
    return duration;
  }
};

let customerDescription = `
  Customer Name: ${customer.name}
  Age: ${customer.calculateAge()}
  Gender: ${customer.gender}
  Room Preferences: ${customer.roomPreferences.join(", ")}
  Payment Method: ${customer.paymentMethod}
  Mailing Address: ${customer.mailingAddress.street}, ${customer.mailingAddress.city}, ${customer.mailingAddress.state} ${customer.mailingAddress.zip}
  Phone Number: ${customer.phoneNumber}
  Check-in Date: ${customer.checkInDate}
  Check-out Date: ${customer.checkOutDate}
  Stay Duration: ${customer.calculateStayDuration()} days
`;

console.log(customerDescription);
