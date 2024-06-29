


// const progressBar = document.getElementById("progress-bar");
// const progressNext = document.getElementById("progress-next");
// const progressPrev = document.getElementById("progress-prev");
// const steps = document.querySelectorAll(".step");
let last_step = 1;
let active = 1;

function progress_next() {
  const steps = document.querySelectorAll(".step");
  active++;
  if (active > steps.length) {
    active = steps.length;
  }
  updateProgres();
}

function progress_perv() {
  const steps = document.querySelectorAll(".step");
  active--;
  if (active < 1) {
    active = 1;
  }
  updateProgres();
}

function updateProgres() {
  const progressNext = document.getElementById("progress-next");
  const progressPrev = document.getElementById("progress-prev");
  const progressBar = document.getElementById("progress-bar");
  const steps = document.querySelectorAll(".step");


  steps.forEach((step, i) => {
    step.classList.remove('pending');
  });
  
  if (active > last_step) {
    steps.forEach((step, i) => {
      if (i < (active - 1)) {
        step.innerHTML = `<i class="fa-solid fa-check"></i>`;
        step.classList.add('active');
      }
    });
    progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";

    steps[active - 1].classList.add('pending');
  } else {
    progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";

    steps[active - 1].classList.remove('active');
    steps[active - 1].innerHTML = active;
    steps[active - 1].classList.add('pending');

    // steps.forEach((step, i) => {
    //   if (i < )
    // });
  }


  // if (active > last_step) {
  //   start = active - 2;
  //   end = active - 1;
  //   steps[start].classList.remove('pending');
  //   sleep(200);
  //   steps[start].classList.add('active');
  //   steps[start].innerHTML = `<i class="fa-solid fa-check"></i>`;
  //   sleep(200)
  //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //   sleep(700);
  //   steps[end].classList.add('pending');


    // steps.forEach((step, i) => {
    //   st = i + 1;
      // if (st < active) {
      //   step.classList.remove('pending')
      //   step.classList.add('active');
      //   step.innerHTML = `<i class="fa-solid fa-check"></i>`;
      // } else {
      //   step.classList.remove('pending');
      //   step.classList.remove('active');
      //   step.innerHTML = st;
      // }
      // if (st == active) {
      //   steps[i - 1].classList.remove('pending');
      //   sleep(200);
      //   steps[i - 1].classList.add('active');
      //   sleep(200)
      //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
      //   sleep(700);
      //   step.classList.add('pending');
      // }

    // });
  // } else {
  //   strat = active;
  //   end = active - 1;
  //   steps[start].classList.remove('pending');
  //   sleep(200);
  //   progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
  //   sleep(700);
  //   steps[end].classList.remove('active');
  //   steps[end].innerHTML = active;
  //   sleep(200);
  //   steps[end].classList.add('pending');
    // stl = steps.length
    // for (i = 1; i <= stl; i++) {
    //   st = stl - i;
    //   if (st > active) {
    //     steps[st].classList.remove('pending');
    //   }
    //   if (st == active) {
    //     steps[st].classList.remove('pending');
    //     sleep(200)
    //     progressBar.style.width = ((active - 1) / (steps.length - 1)) * 100 + "%";
    //     sleep(700);
    //     steps[st].classList.remove('active');
    //     steps[st].innerHTML = st;
    //     sleep(200);
    //     steps[st].classList.add('pending');
    //   }
    // }
    // steps.reverse().forEach((step, i) => {
    //   st = stl - i;

    // });
  // }

  // if (last_step < active) {

  //   setTimeout(() => {
  //     // toggle active class on list items
  //     steps.forEach((step, i) => {
  //       console.log(i)
  //       step.classList.remove("pending")
  //       if (i < (active - 1)) {
  //         step.classList.add("active");
  //         step.innerHTML = `<i class="fa-solid fa-check"></i>`
  //       } else {
  //         step.classList.remove("active");
  //         step.classList.remove("pending")
  //       }
  //     });
  //   }, 500);

  //   // set progress bar width  
  //   progressBar.style.width = 
  //     ((active - 1) / (steps.length - 1)) * 100 + "%";

  //   setTimeout(() => {
  //     // toggle active class on list items
  //     steps.forEach((step, i) => {
  //       if (i == (last_step - 2)) {
  //         step.innerHTML = `<i class="fa-solid fa-check"></i>`
  //       }
  //       if (i < (active - 1)) {
  //         step.classList.remove("pending")
  //         step.classList.add("active");
  //       } else {
  //         step.classList.remove("active");
  //         step.classList.remove("pending")
  //       }
  //       if (i == (active - 1)) {
  //         step.classList.add("pending")
  //         step.innerHTML = active
  //       }
  //     });
  //   }, 500);
  // } else if (last_step > active) {
  //   // toggle active class on list items
  //   steps.forEach((step, i) => {
  //     if (i == (last_step - 1)) {
  //       step.innerHTML = active + 1
  //     }
  //     // if (i == (last_step - 2)) {
  //     //   step.innerHTML = active
  //     // }
  //     if (i < (active - 1)) {
  //       step.classList.remove("pending")
  //       step.classList.add("active");
  //     } else {
  //       step.classList.remove("active");
  //       step.classList.remove("pending")
  //     }
  //     if (i == (active - 1)) {
  //       step.classList.add("pending")
  //       step.innerHTML = active
  //     }

  //   setTimeout(() => {
  //       // set progress bar width  
  //       progressBar.style.width = 
  //       ((active - 1) / (steps.length - 1)) * 100 + "%";
  //     });
  //   }, 500);
  // }
  // // enable disable prev and next buttons
  // if (active === 1) {
  //   progressPrev.disabled = true;
  // } else if (active === steps.length) {
  //   progressNext.disabled = true;
  // } else {
  //   progressPrev.disabled = false;
  //   progressNext.disabled = false;
  // }

  last_step = active;
  console.log(active)
}