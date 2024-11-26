// JSON
const objs = [
  {
    "name": "Sensor 1",
    "status": true,
    "timestamp": "2022-05-05T00:00:00.000Z"
  },
  {
    "name": "Sensor 2",
    "status": false,
    "timestamp": "2022-05-05T00:00:00.000Z"
  },
];

// Gráfico
const rand = () => Math.random();
const x = [1, 2, 3, 4, 5];

// Cria os traços para os dois sensores
let data = objs.slice(0, 2).map((obj, index) => ({
  mode: 'lines',
  line: {color: index === 0 ? "#B57EDC" : "#5D3FD3"}, // Duas cores diferentes
  y: x.map(rand), // Gera valores iniciais para cada traço
  name: obj.name // Nome do sensor como legenda
}));

// Layout do gráfico
var layout = {
  title: 'Status ',
  uirevision: 'true',
  xaxis: {autorange: true},
  yaxis: {autorange: true}
};

// Renderiza o gráfico
Plotly.react('graphDiv', data, layout);
