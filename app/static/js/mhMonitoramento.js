// JSON
const objs = [
  { name: "Sensor 1", status: true },
  { name: "Sensor 2", status: false },
];

// Função para gerar timestamps de 5 em 5 minutos
function generateTimestamps(start, end, interval) {
  const timestamps = [];
  let current = new Date(start);

  while (current <= new Date(end)) {
    timestamps.push(current.toISOString()); // Adiciona o timestamp em formato ISO 8601
    current = new Date(current.getTime() + interval * 60000); // Adiciona 'interval' minutos
  }

  return timestamps;
}

// Gera timestamps de 5 em 5 minutos em um intervalo de 2 horas
const timestamps = generateTimestamps(
  "2024-12-11T00:00:00",
  "2024-12-11T02:00:00",
  5
);

// Gera dados do eixo y alternando entre 1 e 0 para os sensores
const yValues = timestamps.map((_, index) => (index % 2 === 0 ? 1 : 0));

// Gráfico
var trace1 = {
  x: timestamps, // Usar os timestamps gerados no eixo x
  y: yValues, // Usar valores alternados no eixo y
  mode: "lines+markers",
  name: "Status dos Sensores",
  line: { shape: "hv" },
  type: "scatter",
};

var data = [trace1];

var layout = {
  title: "Gráfico com Timestamps de 5 em 5 Minutos",
  xaxis: {
    title: "Horário",
    type: "date", // Especifica que o eixo x é baseado em datas
  },
  yaxis: {
    title: "Status (0 = Desligado, 1 = Ligado)",
  },
  legend: {
    y: 0.5,
    traceorder: "reversed",
    font: { size: 16 },
    yref: "paper",
  },
};

// Renderizar o gráfico
Plotly.newPlot("grafico", data, layout);
