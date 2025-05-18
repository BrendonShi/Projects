console.log("Program started")

let currentChartInitialData = [];

function sendNumbers() {
	console.log("print")
	var input = document.getElementById("snakename");
	var numbersValue = input.value;
	if (numbersValue.trim().length > 0) {
		fetch('/submit', {
			method : 'POST',
			headers: {
				'Accept': 'application/json',
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				number: numbersValue
			})
		})
			.then(response => response.json())
			.then(data => {
				if (data.status === 'success') {
					console.log('Updated numbers:', data.numbers);
					var element = document.getElementById("graph");
					if (element.classList.contains("hidden")) {
						toggle();
					} else {
						console.log('already toggled');
					}

					const nums = data.numbers;
					let initialData;

					if (typeof nums === 'string') {
						const trimmedNums = nums.trim();
						if (trimmedNums === "") {
							initialData = [];
						} else {
							const numArray = trimmedNums.split(',').map(numStr => Number(numStr.trim()));
							initialData = numArray.map(number => ({ value: number }));
						}
					} 
					else {
						initialData = [];
					}

					currentChartInitialData = [...initialData];

					console.log('InitialData: ', initialData);

					const sortedData = [...initialData].sort((a, b) => a.value - b.value); 
					console.log("SortedData: ", sortedData); 

					let currentData = [...sortedData];
					const chartElement = document.getElementById('barChart');

					renderChart(currentData, chartElement, initialData);

				} else {
					console.error(data.message);
				}
			})
			.catch(error => {
				console.error('error:', error);
			});
	} 
}

function toggle() {
	var element = document.getElementById("graph");
	element.classList.remove("hidden");
}

function renderChart(dataToRender, chartElement, originalInitialData) {
	chartElement.innerHTML = '';

	let largestValue = 0;
	if (originalInitialData.length > 0) {
		const values = originalInitialData.map(obj => obj.value);
		const maxVal = Math.max(...values);
		largestValue = maxVal > 0 ? maxVal : 1; 
	} else {
		largestValue = 1;
	}
	console.log("Largest value for scaling: ", largestValue);

	dataToRender.forEach(item => {
		const barHeight = largestValue > 0 ? (item.value / largestValue) * 90 : 0;
		const bar = document.createElement('div');
		bar.className = 'bar';
		bar.style.height = '0';

		const value = document.createElement('div');
		value.className = 'bar-value';
		value.textContent = item.value;
		bar.appendChild(value);

		chartElement.appendChild(bar);

		setTimeout(() => {
			bar.style.height = `${barHeight}%`;
		}, 50);
	});

	barSelection();
}


function updateSelectedValues(values) {
	const numbers = Array.from(values).map(Number).sort((a,b) => a - b);
	let length = numbers.length;

	var total = document.getElementById('total');
	const sum = numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
	total.textContent = sum.toFixed(1);
	console.log("> Total: ", sum);

	var median = document.getElementById('median');
	var medianResult = 0;
	if (length === 0) {
		medianResult = 0;
	} else if (length % 2 === 0) {
		const middle = length / 2;
		medianResult = (numbers[middle - 1] + numbers[middle]) / 2;
	} else {
		const middle = Math.floor(length / 2);
		medianResult = numbers[middle];
	}
	median.textContent = medianResult.toFixed(1);
	console.log("> Median: ", medianResult);

	var mode = document.getElementById('mode');
	const frequency = {};
	let maxCount = 0;
	let modeValue = [];
	if (length > 0) {
		numbers.forEach(num => {
			frequency[num] = (frequency[num] || 0) + 1;
			if (frequency[num] > maxCount) {
				maxCount = frequency[num];
			}
		});
		for (const num in frequency) {
			if (frequency[num] === maxCount) {
				modeValue.push(Number(num));
			}
		}
	}
	mode.textContent = modeValue.length > 0 ? modeValue.join(', ') : "N/A";
	console.log("> Mode: ", modeValue);

	var average = document.getElementById('average');
	const averageResult = length > 0 ? sum / length : 0;
	average.textContent = length > 0 ? averageResult.toFixed(1) : "N/A";
	console.log("> Average: ", averageResult);

	let averageOfInitialData = 0;
	const dataToAverage = currentChartInitialData || [];
	if (dataToAverage.length > 0) {
		const sumOfInitialData = dataToAverage.reduce((acc, item) => {
			const val = Number(item.value);
			return acc + (isNaN(val) ? 0 : val);
		}, 0);
		averageOfInitialData = sumOfInitialData / dataToAverage.length;
	}
	console.log("> Average of all initial data:", averageOfInitialData);

	var totalAverage = document.getElementById('totalAverage');
	totalAverage.textContent = dataToAverage.length > 0 ? averageOfInitialData.toFixed(1) : "N/A";

	var influence = document.getElementById('influence');
	let calculatedInfluenceResult;
	if (length === 0 || dataToAverage.length === 0) {
		calculatedInfluenceResult = 0;
	} else if (averageOfInitialData === 0) {
		calculatedInfluenceResult = (averageResult === 0) ? 0 : Infinity;
	} else {
		calculatedInfluenceResult = (Math.abs(averageResult - averageOfInitialData) / Math.abs(averageOfInitialData)) * 100;
	}

	if (isNaN(calculatedInfluenceResult)) {
		influence.textContent = "N/A";
	} else if (!isFinite(calculatedInfluenceResult)) {
		influence.textContent = "∞";
	} else {
		influence.textContent = calculatedInfluenceResult.toFixed(1) + "%";
	}
	console.log("> Calculated Influence: ", calculatedInfluenceResult);
}

function barSelection() {
	const chartElement = document.getElementById('barChart');
	let isDragging = false;
	const selectedBars = new Set();
	const selectedBarsValues = [];
	const clearButton = document.getElementById('clearSelectionBtn');
	let dragSelectionMode = null;

	const getBarValue = (barElement) => {
		const valueElement = barElement.querySelector('.bar-value');
		if (valueElement && valueElement.textContent !== null && valueElement.textContent.trim() !== "") {
			const num = Number(valueElement.textContent);
			return !isNaN(num) ? num : null;
		}
		return null;
	};

	if (chartElement._eventHandlers) {
		chartElement.removeEventListener('mousedown', chartElement._eventHandlers.mousedown);
		chartElement.removeEventListener('mousemove', chartElement._eventHandlers.mousemove);
		chartElement.removeEventListener('mouseleave', chartElement._eventHandlers.mouseleave);
		chartElement.removeEventListener('mouseup', chartElement._eventHandlers.mouseup);
	}

	const toggleBarSelection = (barElement, shouldSelect) => {
		const value = getBarValue(barElement);
		if (value === null) return;

		if (shouldSelect) {
			if (!barElement.classList.contains('selected')) {
				barElement.classList.add('selected');
				selectedBars.add(barElement);
				selectedBarsValues.push(value);
				updateSelectedValues(selectedBarsValues);
			}
		} else {
			if (barElement.classList.contains('selected')) {
				barElement.classList.remove('selected');
				selectedBars.delete(barElement);
				const index = selectedBarsValues.indexOf(value);
				if (index > -1) {
					selectedBarsValues.splice(index, 1);
				}
				updateSelectedValues(selectedBarsValues);
			}
		}
	};

	const handleMouseDown = (event) => {
		if (event.target === chartElement || event.target.closest('.bar')) {
			isDragging = true;
			chartElement.style.userSelect = 'none';

			const targetBar = event.target.closest('.bar');
			if (targetBar) {
				dragSelectionMode = !targetBar.classList.contains('selected');
				toggleBarSelection(targetBar, dragSelectionMode);
			} else {
				dragSelectionMode = true; 
			}
		}
	};

	const handleMouseMove = (event) => {
		if (!isDragging) return;
		const targetBar = event.target.closest('.bar');
		if (targetBar) {
			const isCurrentlySelected = targetBar.classList.contains('selected');
			if ((dragSelectionMode && !isCurrentlySelected) || (!dragSelectionMode && isCurrentlySelected)) {
				toggleBarSelection(targetBar, dragSelectionMode);
			}
		}
	};

	const handleMouseLeaveOrUp = () => {
		if (isDragging) {
			isDragging = false;
			chartElement.style.userSelect = '';
			dragSelectionMode = null;
		}
	};

	chartElement._eventHandlers = {
		mousedown: handleMouseDown,
		mousemove: handleMouseMove,
		mouseleave: handleMouseLeaveOrUp,
		mouseup: handleMouseLeaveOrUp
	};

	chartElement.addEventListener('mousedown', chartElement._eventHandlers.mousedown);
	chartElement.addEventListener('mousemove', chartElement._eventHandlers.mousemove);
	chartElement.addEventListener('mouseleave', chartElement._eventHandlers.mouseleave);
	document.addEventListener('mouseup', chartElement._eventHandlers.mouseup);

	if (clearButton) {
		clearButton.onclick = () => {
			const currentBarsInDOM = Array.from(chartElement.getElementsByClassName('bar'));
			currentBarsInDOM.forEach(bar => bar.classList.remove('selected'));

			selectedBars.clear();
			selectedBarsValues.length = 0;
			updateSelectedValues(selectedBarsValues);

			console.log("Selection cleared");
		};
	}
}
