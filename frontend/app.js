// c:\Users\Kartik\Downloads\ntcc\plant-disease-app\frontend\app.js

document.addEventListener('DOMContentLoaded', () => {
    
    // API Endpoint config
    const API_URL = '/predict';

    // State Variables
    let selectedImageFile = null;
    let webcamStream = null;
    let activeMode = 'upload'; // 'upload' or 'camera'

    // DOM Elements
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const btnModeUpload = document.getElementById('btn-mode-upload');
    const btnModeCamera = document.getElementById('btn-mode-camera');
    const containerUpload = document.getElementById('container-upload');
    const containerCamera = document.getElementById('container-camera');
    const containerPreview = document.getElementById('container-preview');
    const containerLoading = document.getElementById('container-loading');
    const imagePreview = document.getElementById('image-preview');
    const btnClearImage = document.getElementById('btn-clear-image');
    const btnAnalyzeLeaf = document.getElementById('btn-analyze-leaf');
    
    // Webcam elements
    const videoStream = document.getElementById('webcam-stream');
    const cameraCanvas = document.getElementById('camera-canvas');
    const btnWebcamEnable = document.getElementById('btn-webcam-enable');
    const btnWebcamCapture = document.getElementById('btn-webcam-capture');
    
    // Result elements
    const resultsPlaceholderCard = document.getElementById('results-placeholder-card');
    const resultsCard = document.getElementById('results-card');
    const heatmapSection = document.getElementById('heatmap-section');
    const treatmentSection = document.getElementById('treatment-section');
    
    const resPlant = document.getElementById('res-plant');
    const resDisease = document.getElementById('res-disease');
    const resStatusBadge = document.getElementById('res-status-badge');
    const resStatusBox = document.getElementById('res-status-box');
    const resConfidenceText = document.getElementById('res-confidence-text');
    const resConfidenceLarge = document.getElementById('res-confidence-large');
    const resSeverityText = document.getElementById('res-severity-text');
    const resSeverityIndicator = document.getElementById('res-severity-indicator');
    const resExplanationText = document.getElementById('res-explanation-text');
    
    // Saliency images
    const imgCamOriginal = document.getElementById('img-cam-original');
    const imgCamHeatmap = document.getElementById('img-cam-heatmap');
    const imgCamOverlay = document.getElementById('img-cam-overlay');
    const btnDlOriginal = document.getElementById('btn-dl-original');
    const btnDlHeatmap = document.getElementById('btn-dl-heatmap');
    const btnDlOverlay = document.getElementById('btn-dl-overlay');
    
    // Treatment portal elements
    const infoDescription = document.getElementById('info-description');
    const infoSymptoms = document.getElementById('info-symptoms');
    const infoCauses = document.getElementById('info-causes');
    const infoOrganic = document.getElementById('info-organic');
    const infoChemical = document.getElementById('info-chemical');
    const infoManagement = document.getElementById('info-management');
    
    // History log elements
    const historyTableBody = document.getElementById('history-table-body');
    const btnClearHistory = document.getElementById('btn-clear-history');
    const btnExportPdf = document.getElementById('btn-export-pdf');

    // Setup Event Listeners
    setupModeToggle();
    setupDragAndDrop();
    setupFileSelection();
    setupWebcam();
    setupDiagnosisTrigger();
    setupHistory();
    setupPDFExporter();
    
    // Load existing history logs
    renderHistory();

    /* ==========================================================================
       Mode Toggle Operations (Upload vs Camera)
       ========================================================================== */
    function setupModeToggle() {
        btnModeUpload.addEventListener('click', () => {
            if (activeMode === 'upload') return;
            activeMode = 'upload';
            btnModeUpload.classList.add('active');
            btnModeCamera.classList.remove('active');
            containerUpload.classList.remove('d-none');
            containerCamera.classList.add('d-none');
            stopWebcam();
            resetInferenceUI();
        });

        btnModeCamera.addEventListener('click', () => {
            if (activeMode === 'camera') return;
            activeMode = 'camera';
            btnModeCamera.classList.add('active');
            btnModeUpload.classList.remove('active');
            containerCamera.classList.remove('d-none');
            containerUpload.classList.add('d-none');
            resetInferenceUI();
        });
    }

    /* ==========================================================================
       File Selection & Drag/Drop
       ========================================================================== */
    function setupDragAndDrop() {
        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.add('dragover');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, (e) => {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.remove('dragover');
            }, false);
        });

        dropZone.addEventListener('drop', (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            if (files.length > 0) {
                handleFile(files[0]);
            }
        });
    }

    function setupFileSelection() {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                handleFile(e.target.files[0]);
            }
        });

        btnClearImage.addEventListener('click', () => {
            resetInferenceUI();
        });
    }

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Error: File must be an image.');
            return;
        }
        selectedImageFile = file;
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            containerPreview.classList.remove('d-none');
            containerUpload.classList.add('d-none');
        };
        reader.readAsDataURL(file);
    }

    function resetInferenceUI() {
        selectedImageFile = null;
        imagePreview.src = '#';
        fileInput.value = '';
        containerPreview.classList.add('d-none');
        if (activeMode === 'upload') {
            containerUpload.classList.remove('d-none');
        }
        containerLoading.classList.add('d-none');
        btnAnalyzeLeaf.disabled = false;
        
        // Hide result panels
        resultsCard.classList.add('d-none');
        heatmapSection.classList.add('d-none');
        treatmentSection.classList.add('d-none');
        resultsPlaceholderCard.classList.remove('d-none');
    }

    /* ==========================================================================
       Camera Capture Integration
       ========================================================================== */
    function setupWebcam() {
        btnWebcamEnable.addEventListener('click', async () => {
            try {
                webcamStream = await navigator.mediaDevices.getUserMedia({
                    video: { facingMode: 'environment', width: 640, height: 480 },
                    audio: false
                });
                videoStream.srcObject = webcamStream;
                btnWebcamEnable.classList.add('d-none');
                btnWebcamCapture.classList.remove('d-none');
                document.querySelector('.camera-overlay').classList.add('d-none');
            } catch (err) {
                console.error("Camera access failed: ", err);
                alert("Could not access device camera. Please check permissions or upload a file.");
            }
        });

        btnWebcamCapture.addEventListener('click', () => {
            if (!webcamStream) return;
            
            // Set canvas size equal to video stream feed size
            cameraCanvas.width = videoStream.videoWidth;
            cameraCanvas.height = videoStream.videoHeight;
            
            // Draw current stream frame to canvas
            const ctx = cameraCanvas.getContext('2d');
            ctx.drawImage(videoStream, 0, 0, cameraCanvas.width, cameraCanvas.height);
            
            // Convert canvas data to Blob file
            cameraCanvas.toBlob((blob) => {
                const capturedFile = new File([blob], "captured_leaf.jpg", { type: "image/jpeg" });
                handleFile(capturedFile);
                stopWebcam();
            }, 'image/jpeg', 0.95);
        });
    }

    function stopWebcam() {
        if (webcamStream) {
            webcamStream.getTracks().forEach(track => track.stop());
            webcamStream = null;
        }
        videoStream.srcObject = null;
        btnWebcamEnable.classList.remove('d-none');
        btnWebcamCapture.classList.add('d-none');
        document.querySelector('.camera-overlay').classList.remove('d-none');
    }

    /* ==========================================================================
       Diagnosis & Server Request Handler
       ========================================================================== */
    function setupDiagnosisTrigger() {
        btnAnalyzeLeaf.addEventListener('click', async () => {
            if (!selectedImageFile) {
                alert('Please upload or snap a leaf photo first.');
                return;
            }

            // Enter loading state
            containerPreview.classList.add('d-none');
            containerLoading.classList.remove('d-none');
            btnAnalyzeLeaf.disabled = true;

            // Prepare Form payload
            const formData = new FormData();
            formData.append('file', selectedImageFile);

            try {
                const response = await fetch(API_URL, {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    const errDetail = await response.json();
                    throw new Error(errDetail.detail || 'Failed to complete diagnosis.');
                }

                const result = await response.json();
                
                // Render predictions
                renderDiagnosisResult(result);
                
                // Add to browser local storage history
                saveToHistory(result);
                
            } catch (err) {
                console.error("Diagnosis error: ", err);
                alert(`Error: ${err.message}`);
                containerPreview.classList.remove('d-none');
            } finally {
                containerLoading.classList.add('d-none');
                btnAnalyzeLeaf.disabled = false;
            }
        });
    }

    function renderDiagnosisResult(result) {
        resultsPlaceholderCard.classList.add('d-none');
        resultsCard.classList.remove('d-none');
        heatmapSection.classList.remove('d-none');
        treatmentSection.classList.remove('d-none');

        // Text bindings
        resPlant.textContent = result.plant_name;
        resDisease.textContent = result.disease_name;
        
        // Status Badge settings
        const status = result.status.toLowerCase();
        resStatusBadge.textContent = result.status;
        
        if (status === 'healthy') {
            resStatusBadge.className = 'badge rounded-pill bg-success-glow text-success border border-success-subtle px-3 py-2';
            resStatusBox.style.borderColor = 'rgba(63, 185, 80, 0.2)';
            resDisease.className = 'text-success fw-bold fs-4 text-glow-success';
        } else {
            resStatusBadge.className = 'badge rounded-pill bg-danger-glow text-danger border border-danger-subtle px-3 py-2';
            resStatusBox.style.borderColor = 'rgba(248, 81, 73, 0.2)';
            resDisease.className = 'text-danger-custom fw-bold fs-4 text-glow-danger';
        }

        // Confidence levels (SVG progress ring + large text)
        const percentage = Math.round(result.confidence * 100);
        resConfidenceLarge.textContent = `${(result.confidence * 100).toFixed(2)}%`;
        resConfidenceText.textContent = `${percentage}%`;
        
        // Update SVG Progress Ring
        const circle = document.querySelector('.progress-ring__circle');
        const radius = circle.r.baseVal.value;
        const circumference = radius * 2 * Math.PI;
        circle.style.strokeDasharray = `${circumference} ${circumference}`;
        const offset = circumference - (percentage / 100) * circumference;
        circle.style.strokeDashoffset = offset;
        
        // Update stroke color
        if (status === 'healthy') {
            circle.setAttribute('stroke', '#3fb950');
        } else {
            circle.setAttribute('stroke', '#f85149');
        }

        // Severity levels
        const severity = result.severity.toLowerCase();
        resSeverityText.textContent = result.severity;
        if (severity === 'healthy') {
            resSeverityIndicator.style.color = '#3fb950';
        } else if (severity === 'mild') {
            resSeverityIndicator.style.color = '#58a6ff';
        } else if (severity === 'moderate') {
            resSeverityIndicator.style.color = '#d29922';
        } else {
            resSeverityIndicator.style.color = '#f85149';
        }

        // Explanation text
        resExplanationText.textContent = result.explanation_text;

        // Image bindings
        imgCamOriginal.src = result.images.original;
        imgCamHeatmap.src = result.images.heatmap;
        imgCamOverlay.src = result.images.overlay;
        
        btnDlOriginal.href = result.images.original;
        btnDlHeatmap.href = result.images.heatmap;
        btnDlOverlay.href = result.images.overlay;

        // Populate Treatment accordions
        infoDescription.textContent = result.description;
        
        populateList(infoSymptoms, result.symptoms);
        populateList(infoCauses, result.causes);
        populateList(infoOrganic, result.organic_remedies);
        populateList(infoChemical, result.chemical_remedies);
        
        infoManagement.textContent = result.management_practices;

        // Auto Scroll to Results Card
        resultsCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function populateList(ulElement, listItems) {
        ulElement.innerHTML = '';
        if (!listItems || listItems.length === 0) {
            const li = document.createElement('li');
            li.textContent = "N/A - Non-applicable for this state.";
            ulElement.appendChild(li);
        } else {
            listItems.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                ulElement.appendChild(li);
            });
        }
    }

    /* ==========================================================================
       Local Storage History Management
       ========================================================================== */
    function setupHistory() {
        btnClearHistory.addEventListener('click', () => {
            if (confirm('Are you sure you want to clear the diagnosis history log?')) {
                localStorage.removeItem('plant_diagnosis_history');
                renderHistory();
            }
        });
    }

    function saveToHistory(result) {
        let history = JSON.parse(localStorage.getItem('plant_diagnosis_history') || '[]');
        
        // Add current timestamp
        const entry = {
            id: Date.now(),
            timestamp: new Date().toLocaleString(),
            plant_name: result.plant_name,
            disease_name: result.disease_name,
            status: result.status,
            confidence: result.confidence,
            severity: result.severity,
            images: result.images,
            description: result.description,
            symptoms: result.symptoms,
            causes: result.causes,
            organic_remedies: result.organic_remedies,
            chemical_remedies: result.chemical_remedies,
            management_practices: result.management_practices,
            explanation_text: result.explanation_text
        };
        
        // Prepend to history, max 10 entries
        history.unshift(entry);
        if (history.length > 10) history.pop();
        
        localStorage.setItem('plant_diagnosis_history', JSON.stringify(history));
        renderHistory();
    }

    function renderHistory() {
        const history = JSON.parse(localStorage.getItem('plant_diagnosis_history') || '[]');
        historyTableBody.innerHTML = '';

        if (history.length === 0) {
            const row = document.createElement('tr');
            row.innerHTML = `<td colspan="7" class="text-center py-4 text-muted">No historical scans recorded yet.</td>`;
            historyTableBody.appendChild(row);
            return;
        }

        history.forEach(entry => {
            const row = document.createElement('tr');
            const isHealthy = entry.status.toLowerCase() === 'healthy';
            const statusClass = isHealthy ? 'text-success' : 'text-danger';
            
            row.innerHTML = `
                <td><img src="${entry.images.original}" class="history-thumb" alt="leaf thumb"></td>
                <td class="text-white fw-medium">${entry.plant_name}</td>
                <td><span class="${statusClass} fw-bold">${entry.disease_name}</span></td>
                <td class="fw-semibold">${(entry.confidence * 100).toFixed(1)}%</td>
                <td><span class="badge ${getSeverityBadgeClass(entry.severity)}">${entry.severity}</span></td>
                <td class="fs-8 text-secondary-custom">${entry.timestamp.split(',')[0]}</td>
                <td class="text-end">
                    <button class="btn btn-sm btn-outline-success btn-restore-history rounded-pill px-3" data-id="${entry.id}">
                        <i class="bi bi-folder2-open me-1"></i> Open
                    </button>
                </td>
            `;
            
            // Add click listener to restore button
            row.querySelector('.btn-restore-history').addEventListener('click', () => {
                restoreHistoryItem(entry);
            });
            
            historyTableBody.appendChild(row);
        });
    }

    function getSeverityBadgeClass(severity) {
        const sev = severity.toLowerCase();
        if (sev === 'healthy') return 'bg-success-glow text-success';
        if (sev === 'mild') return 'bg-primary-glow text-primary';
        if (sev === 'moderate') return 'bg-warning-glow text-warning';
        return 'bg-danger-glow text-danger';
    }

    function restoreHistoryItem(entry) {
        // Mock prediction schema to reuse render logic
        const restored = {
            plant_name: entry.plant_name,
            disease_name: entry.disease_name,
            status: entry.status,
            confidence: entry.confidence,
            severity: entry.severity,
            images: entry.images,
            description: entry.description,
            symptoms: entry.symptoms,
            causes: entry.causes,
            organic_remedies: entry.organic_remedies,
            chemical_remedies: entry.chemical_remedies,
            management_practices: entry.management_practices,
            explanation_text: entry.explanation_text
        };
        
        renderDiagnosisResult(restored);
    }

    /* ==========================================================================
       PDF Report Exporter
       ========================================================================== */
    function setupPDFExporter() {
        btnExportPdf.addEventListener('click', () => {
            // Simply invoke print which triggers the printing CSS rules
            window.print();
        });
        
        // Navbar brand trigger to reset UI easily
        document.getElementById('brand-link').addEventListener('click', (e) => {
            e.preventDefault();
            resetInferenceUI();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }
});
