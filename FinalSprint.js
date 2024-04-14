// Define JSON data as a variable // lets use in jsfiddle 
const jsonData = [
    {
        "id": 1,
        "name": "ben kyle",
        "age": 11,
        "email": "benkyle@gmail.com"
    },
    {
        "id": 2,
        "name": "mom dad",
        "age": 12,
        "email": "mom@gmail.com"
    },
    {
        "id": 3,
        "name": "dad mom",
        "age": 13,
        "email": "dad@hotmail.com"
    },
    {
        "id": 4,
        "name": "sam jackson",
        "age": 14,
        "email": "samjackson@yahoo.com"
    },
    {
        "id": 5,
        "name": "eat sideways",
        "age": 15,
        "email": "eatsideways@gmail.com"
    }
];


const data = jsonData;

function getTotalRecords(data) {
    return `Total records: ${data.length}`;
}

function getOldestPerson(data) {
    let oldest = data.reduce((prev, current) => (prev.age > current.age) ? prev : current);
    return `Oldest person: ${oldest.name} (${oldest.age} years old)`;
}

function getEmails(data) {
    let emails = data.map(item => item.email).join(', ');
    return `Emails: ${emails}`;
}

function displayData(data) {
    let html = '';
    data.forEach(item => {
        html += `
            <p>ID: ${item.id}</p>
            <p>Name: ${item.name}</p>
            <p>Age: ${item.age}</p>
            <p>Email: ${item.email}</p>
            <hr>
        `;
    });
    return html;
}
document.getElementById('foreach').innerHTML = displayData(data);

document.getElementById('output').innerHTML = `
    <p>${getTotalRecords(data)}</p>
    <p>${getOldestPerson(data)}</p>
    <p>${getEmails(data)}</p>
`;