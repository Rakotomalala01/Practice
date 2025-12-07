function compact(arr) {
  const result = [];
  arr.filter((element)=>)

  for (let i = 0; i < arr.length; i++) {
    if (arr[i]) {      
      result.push(arr[i]);
    }
  }
  return result;
}

// --------------------------------------------
// TEST CASES
// --------------------------------------------

const tests = [
  [1, 0, "hello", "", null, 5],
  [false, true, undefined, "world", NaN, 42],
  ["", "text", 0, 10, null],
  [null, undefined, false, 0, ""],
  [1, 2, 3]
];

tests.forEach((test, i) => {
  const result = compact(test);
  console.log(`Test #${i + 1}`);
  console.log("Input:  ", test);
  console.log("Output: ", result);
  console.log("------------------------");
});
