// JSON
const objs = [
    {
      "name": "Sensor 1",
      "status": true,
    },
    {
      "name": "Sensor 2",
      "status": false,
    },
  ];
  
// Gráfico
var trace1 = {
  // x: [1, 2, 3, 4],
  // y: [1, 1, 0, 1],
  // array de 0 a 100
  x: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
  // array de 11 elementos de 0 e 1
  y: [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
  mode: 'lines+markers',
  name: 'hv',
  line: {shape: 'hv'},
  type: 'scatter'
};

var data = [trace1];

var layout = {
  legend: {
    y: 0.5,
    traceorder: 'reversed',
    font: {size: 16},
    yref: 'paper'
  }};

Plotly.newPlot('grafico', data, layout);

 
