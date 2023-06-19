let video;
var face_verified = false;
let intervalId;
window.onload = async function(){
    video = document.querySelector('#video');
    
}
Promise.all([
    faceapi.nets.faceRecognitionNet.loadFromUri('static/data_collection/models'),
    faceapi.nets.faceLandmark68Net.loadFromUri('static/data_collection/models'),
    faceapi.nets.ssdMobilenetv1.loadFromUri('static/data_collection/models') //heavier/accurate version of tiny face detector
]).then(start)

async function start() {
    //document.body.append('Models Loaded')
    
    const mediaStream = await navigator.getUserMedia(
        { video:{} },
        stream => video.srcObject = stream,
        err => console.error(err)
    )
    
    //video.src = '../videos/speech.mp4'
    console.log('video added')
    // Stop the media stream track
    if (mediaStream && mediaStream.getVideoTracks().length > 0) {
        const mediaStreamTrack = mediaStream.getVideoTracks()[0];
        mediaStreamTrack.stop();
    }
    await recognizeFaces()
}

async function recognizeFaces() {

    const labeledDescriptors = await loadLabeledImages()
    console.log(labeledDescriptors)
    const faceMatcher = new faceapi.FaceMatcher(labeledDescriptors, 0.7)


    console.log('Playing')
    const canvas = faceapi.createCanvasFromMedia(video)
    // document.body.append(canvas)

    const displaySize = { width: video.width, height: video.height }
    faceapi.matchDimensions(canvas, displaySize)

    //await compareFace(displaySize, canvas, faceMatcher, intervalId)

    intervalId = setInterval(async () => {
        
        await compareFace(displaySize, canvas, faceMatcher, intervalId)

    }, 5000)
}

async function compareFace(displaySize, canvas, faceMatcher, intervalId) {

    const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceDescriptors()

    const resizedDetections = faceapi.resizeResults(detections, displaySize)

    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)

    const results = resizedDetections.map((d) => {
        return faceMatcher.findBestMatch(d.descriptor)
    })

    if(results.length !== 0) {
        for(const result in results){
            const box = resizedDetections[result].detection.box
            const drawBox = new faceapi.draw.DrawBox(box, { label: result.toString() })
            drawBox.draw(canvas)

            const accuracy = (result.distance) * 100;
            

            if(result.label != "unknown") {
                video.pause();
                console.log(accuracy + '%');
                console.log(result)
                console.log(`Face Matched with ${accuracy}% accuracy`);
                face_verified = true;
                // alert("Congratulations! Face is successfully verified")
                // Perform a simple action - stop camera, pop a successful message and move to next page
                
                Swal.fire({
                    title: 'Congratulations! Welcome to UNO',
                    text: 'Exicted to see your profile?',
                    icon: 'success',
                    confirmButtonText: 'Yes, take me in!'
                }).then((result) => {
                    if (result.isConfirmed) {
                      window.open('http://127.0.0.1:8000/profile/', '_self');
                    }
                });
                
            } else {
                face_verified = false;
                // Perform a simple action - stop camera, pop a failed message and move to next page 
                Swal.fire({
                    title: 'Failed!',
                    text: 'sorry, face did not match, Try again?',
                    icon: 'error',
                    confirmButtonText: 'Yes!'
                });
            }
            break;
        }
    } 
    else {
        // Perform a simple action - wait for interval of 1 min to pop a message and remain on same page 
        Swal.fire({
            title: 'Failed!',
            text: 'sorry, No face was detected, Try again?',
            icon: 'error',
            confirmButtonText: 'Yes!'
        });
    }

    // use clearInterval to stop the setInterval function after 5 seconds
    if(face_verified) {
        setTimeout(() => {
            clearInterval(intervalId);
        }, 3000);
    } 
}

async function fetchImg() {
    var imageUrl;
    await fetch(`/image/documents_api/`)
    .then(response => response.json())
    .then(data => {
        console.log(data) 
        data.forEach(element => {
            
            imageUrl = element.doc
        });
    })
    return imageUrl;
}


async function loadLabeledImages() {
    var imageUrl = await fetchImg()
    // var img = document.getElementById('my-image');
    // imageUrl = img.getAttribute("data-image-url");

    // const image = new Image();
    // image.src = imageUrl;

    const labels = ['Kolawole'] // for WebCam
    return Promise.all(
        labels.map(async (label)=>{
            const descriptions = []
            for(let i=1; i<=2; i++) {
                const img = await faceapi.fetchImage(imageUrl)
                const detections = await faceapi.detectSingleFace(img).withFaceLandmarks().withFaceDescriptor()
                //console.log(label + i + JSON.stringify(detections))
                descriptions.push(detections.descriptor)
            }
            //document.body.append(label+' Faces Loaded | ')
            return new faceapi.LabeledFaceDescriptors(label, descriptions)
        })
    )
    


   //let imageUrl = 'static/images/kay.jpeg'
    
}