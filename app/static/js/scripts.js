const objs = [
  {
    name: "Sensor 1",
    status: null,
    detalhes_staus: {
      connected: true,
      disconnected: false,
    },
    timestamp: "2022-05-05T00:00:00.000Z",
  },
  {
    name: "Sensor 2",
    status: null,
    detalhes_staus: {
      connected: true,
      disconnected: false,
    },
    timestamp: "2022-05-05T00:00:00.000Z",
  }
];
//JSON - converter objetos para json 
const jsonData = JSON.stringify(objs)

//JSON - converter json para objetos
const jsonParse = JSON.parse(jsonData)

objData.map((neme) => {
  console.log(neme.detalhes_staus)
})