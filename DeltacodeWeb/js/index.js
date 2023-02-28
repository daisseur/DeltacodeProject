const btn = document.getElementById("done");
let result = document.getElementById("result");
const string = document.getElementById("text");
const shift = document.getElementById("shift");
const password = document.getElementById("password");
const encoding = document.getElementById("encoding");

console.log("started");

function goIt(where) {
  let ip = window.location.hostname;
  console.log(where, ip);
  window.location.assign(where);
}

async function coding(password, string, shift, encoding, result) {
  var myInit = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ string: string, password: password, shift: shift }),
  };
  const res = await fetch(`http://192.168.1.7:5000/${encoding}/encode`, myInit);
  obj = await res.json();

  console.log(obj);
  result.innerText = obj["string"]
}

btn.addEventListener("click", () => {
  console.log("click");
  console.log(
    password.value,
    string.value,
    parseInt(shift.value),
    "after",
    encoding.value
  );
  let data = coding(
    password.value,
    string.value,
    parseInt(shift.value),
    encoding.value,
    result
  );
});
