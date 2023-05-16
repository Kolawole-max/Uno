const prevBtns = document.querySelectorAll(".btn-prev");
const nextBtns = document.querySelectorAll(".btn-next");
const progress = document.getElementById("progress");
const formSteps = document.querySelectorAll(".form-step");
const progressSteps = document.querySelectorAll(".progress-step");

let formStepsNum = 1;


nextBtns.forEach((btn) => {
  btn.addEventListener("click", () => {    
      formStepsNum++;
      updateFormSteps();
      updateProgressbar();
    
    
     
    if(formStepsNum == 2){
      let firstName = document.getElementById("first-name").value;
      let lastName = document.getElementById("last-name").value;
      let otherName = document.getElementById("other-name").value;
      let contactNumber = document.getElementById("contact-number").value;
      let gender = document.getElementById("gender").value;
      let marital = document.getElementById("marital").value;
      let occupation = document.getElementById("occupation").value;

            
    }
    if(formStepsNum == 3){
      alert("3");
    }
    if(formStepsNum == 4){
      alert("4");
    }
    
  });
});

prevBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    formStepsNum--;
    updateFormSteps();
    updateProgressbar();
  });
});

function updateFormSteps() {
  formSteps.forEach((formStep) => {
    formStep.classList.contains("form-step-active") &&
      formStep.classList.remove("form-step-active");
  });

  formSteps[formStepsNum].classList.add("form-step-active");
}

function updateProgressbar() {
  progressSteps.forEach((progressStep, idx) => {
    if (idx < formStepsNum + 1) {
      progressStep.classList.add("progress-step-active");
    } else {
      progressStep.classList.remove("progress-step-active");
    }
  });

  const progressActive = document.querySelectorAll(".progress-step-active");

  progress.style.width =
    ((progressActive.length - 1) / (progressSteps.length - 1)) * 100 + "%";
}

let add_more = document.getElementById('btn-add-more');
let survey_options = document.getElementById('survey-options');


 

// var video = document.querySelector('#video');
// var startRecord = document.querySelector('#startRecord');
// var stopRecord = document.querySelector('#stopRecord');
// var downloadLink = document.querySelector('#downloadLink');
// var videoscreen = document.querySelector('#videoscreen');

// window.onload = async function(){
//   stopRecord.style.display = "none";
//   videoscreen.style.display = "none";
//   videoStream = await navigator.mediaDevices.getUserMedia({video:true});
//   video.srcObject = videoStream;

// }

// startRecord.onclick = function () {
//     startRecord.style.display = 'none';
//     stopRecord.style.display = 'inline';


//     MediaRecorder = new MediaRecorder(videoStream);

//     let blob = [];
//     MediaRecorder.addEventListener('dataavailable', function (e) {
//       blob.push(e.data);
//       })

//     MediaRecorder.addEventListener('stop', function() {
//       var videoLocal = URL.createObjectURL(new Blob(blob));
//        videoscreen.src = videoLocal;
//       // downloadLink.href = videoLocal;
//     })

//     MediaRecorder.start();
// }

// stopRecord.onclick = function () {
//   MediaRecorder.stop();
//   video.style.display = "none";
//   videoscreen.style.display = "inline";
 
//   }
