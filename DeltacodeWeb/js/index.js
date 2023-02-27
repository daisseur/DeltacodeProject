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

async function coding(password, string, shift, encoding) {
  var myInit = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ string: string, password: password, shift: shift }),
  };
  var obj = await fetch(`http://192.168.1.7:5000/${encoding}/encode`, myInit)
    .then((res) => {
      return res.json();
    })
    .then((jsonResponse) => {
      console.log(jsonResponse);
      return jsonResponse;
    })
    .catch((err) => {
      // handle error
      console.error(err);
      return err;
    });
  console.log("222", obj)
  return await obj
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
    encoding.value
  );
  console.log(data);
  result.innerText = data;
});
