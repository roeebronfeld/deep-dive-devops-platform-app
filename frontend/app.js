const healthStatus = document.getElementById("health-status");
const deploymentSummary = document.getElementById("deployment-summary");
const podsList = document.getElementById("pods-list");

async function fetchJson(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }

  return response.json();
}

function renderHealth(data) {
  healthStatus.textContent = `${data.service}: ${data.status}`;
}

function renderPods(data) {
  deploymentSummary.textContent = JSON.stringify(data.deployment, null, 2);

  podsList.innerHTML = "";

  data.pods.forEach((pod) => {
    const item = document.createElement("li");
    item.textContent =
      `${pod.name} - ${pod.phase} - ready: ${pod.ready} - ` +
      `restarts: ${pod.restartCount} - node: ${pod.nodeName} - ageSeconds: ${pod.ageSeconds}`;
    podsList.appendChild(item);
  });
}

function renderError(error) {
  const message = `Could not reach backend: ${error.message}`;

  healthStatus.textContent = message;
  healthStatus.className = "error";
  deploymentSummary.textContent = message;
  deploymentSummary.className = "error";
  podsList.innerHTML = `<li class="error">${message}</li>`;
}

async function loadPage() {
  try {
    const [health, pods] = await Promise.all([
      fetchJson("/health"),
      fetchJson("/pods"),
    ]);

    renderHealth(health);
    renderPods(pods);
  } catch (error) {
    renderError(error);
  }
}

loadPage();
