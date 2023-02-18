const btn = document.getElementById("done");
const result = document.getElementById("result");

console.log("started");

function goIt(where) {
  let ip = window.location.hostname;
  console.log(where, ip);
  window.location.assign(where);
}

function get_encode(password, string) {
  var myInit = {method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({"string": string, "password": password})};
  fetch("http://127.0.0.1:5000/DayEncoding/encode", myInit).then((res) => { 
    return res.json() 
  })
  .then((jsonResponse) => {
    console.log(jsonResponse);
  })
  .catch((err) => {
    // handle error
    console.error(err);
  });
}

btn.addEventListener("click", () => {
  console.log("click");
  get_encode("mdp", "coucou")
  result.innerText = "DONE";
});
