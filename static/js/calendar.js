"use strict";

const dailyTable = document.querySelector(".daily_table");
 {% for group in groups %}
    let kursDb = [
      {% for kurs in group.kurslar %}
        {
          nomi: "{{kurs.nomi}}",
          teacher: "{{kurs.teacher}}",
          xona: "{{kurs.xona}}",
          boshlanish: "{{kurs.boshlanish}}",
          tugash: "{{kurs.tugash}}",
          rang: "{{kurs.rang}}",
          kursNomi: "{{kurs.kursNomi}}",
          kurs_boshlanish: "{{kurs.kurs_boshlanish}}",
          kurs_tugashi: "{{kurs.kurs_tugashi}}",
          talabalar_soni: "{{kurs.talabalar_soni}}",
        },
      {% endfor %}
    ];
  {% endfor %}

let xonaDb = [
  "1-xona",
  "2-xona",
  "Informatika xona",
  "Sport zal",
  "5-xona",
  "6-xona",
  "Kutubxona",
];

for (let i = 0; i < xonaDb.length; i++) {
  let xonaTr = document.createElement("tr");
  xonaTr.className = `table_room_${i + 1}-xona`;
  let xonaRowName = document.createElement("td");
  xonaRowName.textContent = xonaDb[i];
  xonaTr.appendChild(xonaRowName);
  for (let y = 0; y < 31; y++) {
    let xonaRow = document.createElement("td");
    xonaTr.appendChild(xonaRow);
  }
  dailyTable.appendChild(xonaTr);
}

kursDb.forEach((kurs) => {
  kurs.height = 100;

  let cardXona = document.querySelector(`.table_room_${kurs.xona}`);
  let cardXonaTd = document.querySelectorAll(`.table_room_${kurs.xona}`)[0];

  let cardXonaElement = document.createElement("div");
  cardXonaElement.className = "kursCard";

  const cardXonaName = document.createElement("div");
  cardXonaName.className = "cardXonaName";
  cardXonaName.textContent = kurs.kursNomi;
  cardXonaElement.appendChild(cardXonaName);
  const cardXonaGroup = document.createElement("div");
  cardXonaGroup.className = "cardXonaGroup";
  cardXonaGroup.textContent = kurs.nomi;
  cardXonaElement.appendChild(cardXonaGroup);
  const cardXonaTeacher = document.createElement("div");
  cardXonaTeacher.className = "cardXonaTeacher";
  cardXonaTeacher.textContent = kurs.teacher;
  cardXonaElement.appendChild(cardXonaTeacher);
  const cardXonaMuddat = document.createElement("div");
  cardXonaMuddat.className = "cardXonaMuddat";
  cardXonaMuddat.textContent = `${kurs.kurs_boshlanish.substring(
    0,
    5
  )} - ${kurs.kurs_tugashi.substring(0, 5)}`;
  cardXonaElement.appendChild(cardXonaMuddat);
  const cardXonaStudentNumber = document.createElement("div");
  cardXonaStudentNumber.className = "cardXonaStudentNumber";
  cardXonaStudentNumber.textContent = kurs.talabalar_soni;
  cardXonaElement.appendChild(cardXonaStudentNumber);

  let soat = parseInt(kurs.boshlanish.substring(0, 2));
  let minut = parseInt(kurs.boshlanish.substring(3, 5));
  let soat1 = parseInt(kurs.tugash.substring(0, 2));
  let minut1 = parseInt(kurs.tugash.substring(3, 5));

  let leftMargin = 100 + (soat - 7) * 200;
  let minut2 = 0;

  if (minut == 30) {
    leftMargin += 100;
  }

  if (minut1 - minut == 30) {
    minut2 = 0.5;
  }

  let uzunlik = (soat1 - soat) * 200 + minut2 * 200;

  cardXonaElement.style.left = `${leftMargin}px`;
  cardXonaElement.style.backgroundColor = "blue";
  cardXona.appendChild(cardXonaElement);
  cardXonaElement.style.backgroundColor = kurs.rang;
  cardXonaElement.style.width = `${uzunlik}px`;
  cardXonaTd.style.height = `${cardXonaElement.offsetHeight}px`;
  if (cardXonaElement.offsetHeight > kurs.height) {
    cardXonaTd.style.height = `${cardXonaElement.offsetHeight}px`;
  }
});
