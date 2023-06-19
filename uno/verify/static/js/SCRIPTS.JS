const video = await faceapi.getVideoInput();
document.body.append(video);

Promise.all([
    faceapi.nets.faceRecognitionNet.loadFromUri('static/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('static/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('static/models') //heavier/accurate version of tiny face detector
]).then(start)

const faceImage = await faceapi.fetchImage('path/to/known/face.jpg');
const knownFace = await faceapi.detectSingleFace(faceImage).withFaceLandmarks().withFaceDescriptor();

video.addEventListener('play', async () => {
  const canvas = faceapi.createCanvasFromMedia(video);
  document.body.append(canvas);
  const displaySize = { width: video.width, height: video.height };
  faceapi.matchDimensions(canvas, displaySize);

  setInterval(async () => {
    const detections = await faceapi.detectSingleFace(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceDescriptor();
    if (!detections) return;
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    const distance = faceapi.round(faceapi.euclideanDistance(knownFace.descriptor, resizedDetections.descriptor));
    const accuracy = (1 - distance) * 100;
    console.log(accuracy + '%');
  }, 1000);
});
