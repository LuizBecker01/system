// JSON - exemplo de dados
const objs = [
  {
    name: "Sensor 1",
    status: null,
    detalhes_status: {
      connected: true,
      disconnected: false,
    },
    timestamp: "2022-05-05T00:00:00.000Z",
  },
  {
    name: "Sensor 2",
    status: null,
    detalhes_status: {
      connected: true,
      disconnected: false,
    },
    timestamp: "2022-05-05T00:00:00.000Z",
  }
];

// JSON - converter objetos para json 
const jsonData = JSON.stringify(objs)

// JSON - converter json para objetos
const jsonParse = JSON.parse(jsonData)

document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("grafico").getContext("2d");

  // Requisição para pegar os dados do JSON
  fetch("/dados")
    .then(response => response.json())
    .then(dados => {
      // Exibe os dados para depuração no contêiner
      const container = document.getElementById("dados-container");
      container.innerHTML = `<pre>${JSON.stringify(dados, null, 2)}</pre>`;

      // Prepara os rótulos e os dados
      const labels = dados.map(item => item.name);  // Usando 'name' como rótulo
      const dataAtivo = dados.map(item => {
        // Ajusta o valor de status para 1 ou 0
        if (item.status === true) {
          return 1;
        } else if (item.status === false) {
          return 0;
        }
        return null;  // Tratar quando status for null
      });

      // Criação do gráfico
      new Chart(ctx, {
        type: 'line',  // Gráfico de linha
        data: {
          labels: labels,  // Nomes dos sensores como rótulos
          datasets: [{
            label: 'Status dos Equipamentos',
            data: dataAtivo,  // Status dos equipamentos como dados
            borderColor: '#36a2eb',  // Cor da linha
            backgroundColor: 'rgba(54, 162, 235, 0.2)',  // Cor do fundo da linha
            fill: true,  // Preenchimento da área abaixo da linha
            tension: 0.4,a
          }]
        },
        options: {
          responsive: true,  // Gráfico responsivo
          plugins: {
            legend: {
              labels: {
                color: '#fff'  // Cor da legenda
              }
            }
          },
          scales: {
            x: {
              ticks: {
                color: '#fff'  // Cor das legendas do eixo X
              }
            },
            y: {
              beginAtZero: true,
              ticks: {
                color: '#fff'  // Cor das legendas do eixo Y
              }
            }
          }
        }
      });
    })
    .catch(error => {
      // console.error("Erro ao carregar dados:", error);
      document.getElementById("dados-container").innerHTML = "<p>Erro ao carregar os dados.</p>";
    });
});