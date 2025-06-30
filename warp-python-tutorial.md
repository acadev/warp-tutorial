# Warp AI Terminal Tutorial: Python Development Made Simple

Welcome to this comprehensive tutorial on using Warp's AI-powered terminal for Python development! This guide will walk you through Warp's most powerful features, designed especially for beginners to Python coding.

## What You'll Learn

- **Agentic Coding**: Let Warp's AI Agent write, modify, and debug code for you
- **Interactive Development**: Use Warp's smart features for real-time coding assistance
- **Debugging & Testing**: Identify and fix issues with AI assistance
- **Workflows**: Streamline your development process with Warp's automation features
- **Notebooks**: Create executable documentation and tutorials

## Prerequisites

- Basic familiarity with using a terminal
- Python 3.7+ installed on your system
- No prior Python experience required!

---

## Part 1: Setting Up Your Development Environment

Let's start by creating a new Python project and setting up our workspace.

```warp-runnable-command
mkdir warp-python-demo && cd warp-python-demo
```

```warp-runnable-command
python3 --version
```

### Creating a Virtual Environment

It's a best practice to use virtual environments for Python projects:

```warp-runnable-command
python3 -m venv tutorial_env
```

```warp-runnable-command
source tutorial_env/bin/activate
```

---

## Part 2: Agentic Coding - Let AI Write Your Code

One of Warp's most powerful features is its AI Agent that can write complete programs for you. Let's demonstrate this by asking the AI to create different types of Python applications.

### Example 1: Simple Calculator

**Try this**: In Warp's command line, type:
```
@agent Create a Python calculator that can perform basic arithmetic operations (add, subtract, multiply, divide) with error handling
```

The AI Agent will:
1. Create a complete Python file
2. Include proper error handling
3. Add comments explaining the code
4. Make it user-friendly for beginners

### Example 2: File Organizer

**Try this**: Ask the agent to create a more complex program:
```
@agent Create a Python script that organizes files in a directory by their extensions, moving them into appropriate folders
```

### Example 3: Data Analysis Tool

**Try this**: For something more advanced:
```
@agent Create a Python script that reads a CSV file, analyzes the data, and creates simple visualizations using matplotlib
```

---

## Part 3: Interactive Development and Real-time Assistance

Warp provides intelligent suggestions and auto-completion as you code. Let's explore these features.

### Smart Command Completion

Try typing these commands and notice how Warp suggests completions:

```warp-runnable-command
pip install {{package_name}}
```

```warp-runnable-command
python -m {{module_name}}
```

### AI-Powered Command Suggestions

When you're unsure about a command, just describe what you want to do:

**Examples to try:**
- "How do I install a Python package?"
- "How do I run a Python script?"
- "How do I check what Python packages are installed?"

---

## Part 4: Debugging and Error Resolution

Let's create a program with intentional bugs and see how Warp helps us fix them.

```warp-runnable-command
cat > buggy_program.py << 'EOF'
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # Bug: division by zero if empty list

def process_user_input():
    user_input = input("Enter numbers separated by commas: ")
    numbers = user_input.split(",")
    # Bug: strings not converted to numbers
    return numbers

def main():
    numbers = process_user_input()
    avg = calculate_average(numbers)
    print(f"The average is: {avg}")

if __name__ == "__main__":
    main()
EOF
```

```warp-runnable-command
python buggy_program.py
```

When you encounter errors, you can ask Warp's AI Agent to help:

**Try asking:**
```
@agent Fix the errors in buggy_program.py and explain what was wrong
```

---

## Part 5: Testing and Quality Assurance

Let's create a complete project with tests to demonstrate Warp's testing capabilities.

### Creating a Simple Library

**Ask the agent:**
```
@agent Create a Python module called 'math_utils.py' with functions for basic mathematical operations, and create a separate test file using pytest
```

### Running Tests

```warp-runnable-command
pip install pytest
```

```warp-runnable-command
pytest test_math_utils.py -v
```

### Code Quality Checks

```warp-runnable-command
pip install flake8 black
```

```warp-runnable-command
flake8 math_utils.py
```

```warp-runnable-command
black math_utils.py
```

---

## Part 6: Workflows and Automation

Warp can help automate common development workflows. Let's create some useful automation scripts.

### Automated Project Setup

**Ask the agent:**
```
@agent Create a Python script that sets up a new Python project with a virtual environment, requirements.txt, and basic project structure
```

### Git Workflow Automation

```warp-runnable-command
git init
```

```warp-runnable-command
git add .
```

```warp-runnable-command
git commit -m "Initial commit: Warp tutorial project"
```

**Try asking:**
```
@agent Create a script that automates the git workflow: staging, committing with a descriptive message, and pushing to remote
```

---

## Part 7: Advanced Features

### Working with APIs

**Ask the agent:**
```
@agent Create a Python script that fetches data from a public API (like JSONPlaceholder) and saves it to a JSON file
```

### Database Integration

**Ask the agent:**
```
@agent Create a simple Python script that creates a SQLite database, adds sample data, and queries it
```

### Web Scraping Example

**Ask the agent:**
```
@agent Create a Python web scraper using requests and BeautifulSoup that extracts data from a simple webpage
```

---

## Part 8: Multi-Agent Workflows and Agent Management

One of Warp's most powerful features is the ability to work with multiple AI agents simultaneously. This allows you to orchestrate complex development workflows where different agents handle different aspects of your project.

### Understanding Agent Management

Warp's agent management system allows you to:
- Create multiple specialized agents for different tasks
- Switch between agents seamlessly
- Coordinate work across multiple agents
- Maintain context across different development phases

### Setting Up Multi-Agent Workflows

Let's explore how to use multiple agents effectively in a real development scenario.

#### Scenario: Building a Complete Web Application

We'll create a simple web application using multiple agents, each specializing in different aspects:

1. **Backend Agent** - Handles API development and database work
2. **Frontend Agent** - Manages HTML, CSS, and JavaScript
3. **Testing Agent** - Creates and runs comprehensive tests
4. **DevOps Agent** - Handles deployment and infrastructure

### Agent 1: Backend Development

**Start a new agent session for backend work:**

```warp-runnable-command
# Let's create our project structure first
mkdir multi-agent-webapp && cd multi-agent-webapp
mkdir backend frontend tests deployment
```

**Now ask the Backend Agent to create the API:**
```
@agent:backend Create a Flask REST API in the backend/ directory with endpoints for user management (CRUD operations). Include a SQLite database setup and proper error handling.
```

**The Backend Agent will typically create:**
- `backend/app.py` - Main Flask application
- `backend/models.py` - Database models
- `backend/requirements.txt` - Python dependencies
- `backend/config.py` - Configuration settings

### Agent 2: Frontend Development

**Switch to a Frontend Agent for client-side work:**
```
@agent:frontend Create a simple HTML/CSS/JavaScript frontend in the frontend/ directory that interacts with our Flask API. Include forms for creating and editing users, and a table to display all users.
```

**The Frontend Agent will create:**
- `frontend/index.html` - Main HTML page
- `frontend/styles.css` - Styling
- `frontend/script.js` - JavaScript for API interactions
- `frontend/components/` - Reusable UI components

### Agent 3: Testing and Quality Assurance

**Engage a Testing Agent for comprehensive test coverage:**
```
@agent:testing Create comprehensive tests for our web application in the tests/ directory. Include unit tests for the Flask API, integration tests for the full stack, and end-to-end tests using Selenium.
```

**The Testing Agent will create:**
- `tests/test_api.py` - Backend API tests
- `tests/test_frontend.py` - Frontend functionality tests
- `tests/test_integration.py` - Full-stack integration tests
- `tests/conftest.py` - Test configuration and fixtures

### Agent 4: DevOps and Deployment

**Finally, use a DevOps Agent for deployment setup:**
```
@agent:devops Create deployment configurations in the deployment/ directory. Include Docker containers for the application, a docker-compose setup for local development, and a simple deployment script.
```

**The DevOps Agent will create:**
- `deployment/Dockerfile.backend` - Backend container
- `deployment/Dockerfile.frontend` - Frontend container
- `deployment/docker-compose.yml` - Multi-container setup
- `deployment/deploy.sh` - Deployment automation script

### Coordinating Between Agents

#### Agent Handoffs and Context Sharing

When working with multiple agents, you can create seamless handoffs:

**Example 1: Backend to Testing Handoff**
```
@agent:backend I've created a Flask API with user management endpoints. Can you document the API endpoints and their expected responses?

# Then switch to testing agent
@agent:testing Based on the Flask API created by the backend agent, create comprehensive API tests that cover all endpoints, error cases, and edge cases.
```

**Example 2: Frontend to Backend Coordination**
```
@agent:frontend The frontend needs to handle user authentication. What endpoints should I expect from the backend?

@agent:backend Based on the frontend requirements, add JWT authentication endpoints to the existing Flask API, including login, logout, and token refresh.
```

#### Cross-Agent Collaboration Commands

**Collaborative Debugging:**
```warp-runnable-command
# Run the backend
cd backend && python app.py &
BACKEND_PID=$!
```

```warp-runnable-command
# Serve the frontend
cd frontend && python -m http.server 8080 &
FRONTEND_PID=$!
```

**Now ask multiple agents to help debug:**
```
@agent:backend The API is returning 500 errors. Can you check the backend logs and identify the issue?

@agent:frontend The frontend can't connect to the API. Can you verify the JavaScript fetch calls are correctly formatted?

@agent:testing Can you create a test that reproduces this connection issue between frontend and backend?
```

### Advanced Multi-Agent Patterns

#### Pattern 1: Parallel Development

**Simultaneous feature development:**
```
# Agent 1 works on user authentication
@agent:auth Implement OAuth2 authentication with Google and GitHub providers in the backend.

# Agent 2 works on data visualization
@agent:viz Create interactive charts and graphs for user data using Chart.js in the frontend.

# Agent 3 works on API optimization
@agent:perf Optimize database queries and add caching to improve API performance.
```

#### Pattern 2: Code Review Chain

**Multi-agent code review process:**
```
@agent:security Review the authentication code for security vulnerabilities and suggest improvements.

@agent:performance Analyze the current codebase for performance bottlenecks and optimization opportunities.

@agent:testing Based on the security and performance reviews, create additional tests to cover the identified concerns.
```

#### Pattern 3: Incremental Feature Building

**Building features step-by-step with different agents:**
```
# Step 1: Database design
@agent:db Design a database schema for a blog feature with posts, comments, and tags.

# Step 2: API development
@agent:api Implement REST endpoints for the blog schema created by the database agent.

# Step 3: Frontend implementation
@agent:ui Create a blog interface that uses the API endpoints from the API agent.

# Step 4: Testing
@agent:qa Create comprehensive tests for the entire blog feature pipeline.
```

### Agent Management Best Practices

#### 1. Clear Agent Specialization
```
# Good: Specific agent roles
@agent:frontend Handle all React component development
@agent:backend Manage Python/Django API development
@agent:mobile Work on React Native mobile app

# Avoid: Generic agents that handle everything
@agent Do all the development work
```

#### 2. Context Preservation
```
# Maintain context when switching agents
@agent:backend Remember that we're using PostgreSQL with SQLAlchemy ORM for this project

@agent:frontend Keep in mind that the backend uses JWT tokens for authentication
```

#### 3. Agent Communication
```
# Cross-reference between agents
@agent:testing Create tests for the user authentication flow that the backend agent implemented

@agent:docs Document the API endpoints that the backend agent created for the frontend agent
```

### Practical Multi-Agent Exercise

**Let's build a complete feature using multiple agents:**

#### Exercise: Real-time Chat Application

**Step 1: Architecture Planning**
```
@agent:architect Design the overall architecture for a real-time chat application with user rooms, message history, and online status.
```

**Step 2: Backend Implementation**
```
@agent:backend Implement a WebSocket-based chat server using Flask-SocketIO with room management and message persistence.
```

**Step 3: Frontend Development**
```
@agent:frontend Create a responsive chat interface using vanilla JavaScript and Socket.IO client that connects to the backend.
```

**Step 4: Real-time Features**
```
@agent:realtime Add typing indicators, online user lists, and message read receipts to both frontend and backend.
```

**Step 5: Testing**
```
@agent:testing Create tests for WebSocket connections, message delivery, room management, and concurrent user scenarios.
```

**Step 6: Deployment**
```
@agent:deploy Set up production deployment with proper WebSocket support, load balancing, and monitoring.
```

### Monitoring Multi-Agent Progress

**Track progress across agents:**
```warp-runnable-command
# Create a simple progress tracker
echo "# Multi-Agent Development Progress" > progress.md
echo "## Backend Agent Tasks" >> progress.md
echo "- [ ] User authentication API" >> progress.md
echo "- [ ] Database models" >> progress.md
echo "- [ ] WebSocket implementation" >> progress.md
echo "" >> progress.md
echo "## Frontend Agent Tasks" >> progress.md
echo "- [ ] Chat interface" >> progress.md
echo "- [ ] Real-time updates" >> progress.md
echo "- [ ] User management UI" >> progress.md
echo "" >> progress.md
echo "## Testing Agent Tasks" >> progress.md
echo "- [ ] Unit tests" >> progress.md
echo "- [ ] Integration tests" >> progress.md
echo "- [ ] E2E tests" >> progress.md
```

**View progress:**
```warp-runnable-command
cat progress.md
```

### Troubleshooting Multi-Agent Workflows

#### Common Issues and Solutions

**Issue 1: Conflicting Code Changes**
```
@agent:merge I have conflicting changes from the backend and frontend agents. Can you help resolve the merge conflicts and ensure compatibility?
```

**Issue 2: Inconsistent API Contracts**
```
@agent:api-design Review the API endpoints created by different agents and standardize the request/response formats for consistency.
```

**Issue 3: Integration Problems**
```
@agent:integration The frontend and backend components created by different agents aren't working together. Can you identify and fix the integration issues?
```

### Advanced Agent Orchestration

#### Creating Agent Workflows

**Sequential workflow:**
```bash
# Define a complete development pipeline
echo "Starting multi-agent development pipeline..."

# Phase 1: Planning
@agent:analyst Analyze requirements and create detailed specifications

# Phase 2: Architecture
@agent:architect Design system architecture based on analyst specifications

# Phase 3: Development
@agent:backend Implement backend based on architecture design
@agent:frontend Implement frontend based on architecture design

# Phase 4: Integration
@agent:integration Integrate frontend and backend components

# Phase 5: Testing
@agent:testing Create comprehensive test suite for integrated application

# Phase 6: Deployment
@agent:devops Set up deployment pipeline and monitoring
```

#### Agent Collaboration Templates

**Template 1: Feature Development**
```
# Feature: {{feature_name}}
# Lead Agent: {{lead_agent}}
# Supporting Agents: {{supporting_agents}}

@agent:{{lead_agent}} Lead the development of {{feature_name}} feature
@agent:{{support_agent_1}} Support the lead agent with {{specific_task_1}}
@agent:{{support_agent_2}} Support the lead agent with {{specific_task_2}}
```

**Template 2: Bug Fix Workflow**
```
# Bug: {{bug_description}}
# Priority: {{priority_level}}

@agent:debug Identify the root cause of: {{bug_description}}
@agent:fix Implement a solution for the identified issue
@agent:test Create tests to prevent regression of this bug
@agent:review Review the fix for potential side effects
```

### Multi-Agent Development Metrics

**Track agent productivity:**
```warp-runnable-command
# Create a simple metrics tracker
cat > agent_metrics.py << 'EOF'
#!/usr/bin/env python3
import json
from datetime import datetime

def log_agent_activity(agent_name, task, status):
    """Log agent activity for metrics tracking"""
    activity = {
        'timestamp': datetime.now().isoformat(),
        'agent': agent_name,
        'task': task,
        'status': status
    }
    
    try:
        with open('agent_log.json', 'r') as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
    
    logs.append(activity)
    
    with open('agent_log.json', 'w') as f:
        json.dump(logs, f, indent=2)
    
    print(f"Logged: {agent_name} - {task} - {status}")

if __name__ == "__main__":
    # Example usage
    log_agent_activity("backend", "API development", "completed")
    log_agent_activity("frontend", "UI design", "in_progress")
    log_agent_activity("testing", "Unit tests", "pending")
EOF
```

```warp-runnable-command
python agent_metrics.py
```

### Agent Management Tips

#### 1. **Maintain Clear Boundaries**
- Each agent should have specific expertise areas
- Avoid overlapping responsibilities
- Use handoffs for cross-domain work

#### 2. **Document Agent Decisions**
```warp-runnable-command
echo "# Agent Decision Log" > agent_decisions.md
echo "## Backend Agent Decisions" >> agent_decisions.md
echo "- Chose Flask over Django for simplicity" >> agent_decisions.md
echo "- Used SQLite for development, PostgreSQL for production" >> agent_decisions.md
echo "## Frontend Agent Decisions" >> agent_decisions.md
echo "- Implemented vanilla JavaScript instead of framework" >> agent_decisions.md
echo "- Used CSS Grid for layout" >> agent_decisions.md
```

#### 3. **Regular Agent Sync Points**
```
# Daily agent sync
@agent:lead Summarize progress from all agents and identify any blocking issues

# Weekly agent review
@agent:review Review code quality and consistency across all agents' work

# Sprint agent retrospective
@agent:retro Analyze what worked well and what could be improved in our multi-agent workflow
```

---

## Part 9: Computational Biology and Molecular Dynamics Simulations

Warp's multi-agent capabilities shine when handling complex computational workflows. Let's explore how to set up and run molecular dynamics simulations to study protein-protein interactions, specifically the Nsp10-Nsp16 complex from SARS-CoV-2.

### Scientific Background: Nsp10-Nsp16 Complex

The Nsp10-Nsp16 complex is crucial for SARS-CoV-2 viral replication. Understanding their interaction mechanism could inform drug design strategies. We'll use computational methods to:

1. **Hypothesis**: The binding interface between Nsp10 and Nsp16 involves specific hydrogen bonds and hydrophobic interactions that stabilize the complex
2. **Validation**: Use molecular dynamics simulations to study binding stability and identify key residues
3. **Analysis**: Quantify binding energies and interaction patterns

### Setting Up the Computational Environment

**Create a dedicated computational biology workspace:**

```warp-runnable-command
mkdir computational-biology && cd computational-biology
mkdir structures simulations analysis results notebooks
```

**Install the computational biology stack:**

```warp-runnable-command
# Create a dedicated conda environment for computational biology
conda create -n compbio python=3.9 -y
conda activate compbio
```

```warp-runnable-command
# Install OpenMM and related packages
conda install -c conda-forge openmm pdbfixer mdtraj nglview -y
pip install biotite py3Dmol matplotlib seaborn pandas numpy scipy
```

### Multi-Agent Computational Workflow

#### Agent 1: Structure Preparation and Analysis

**Ask the Structure Agent to prepare the system:**
```
@agent:structure Download the Nsp10-Nsp16 complex structure from PDB (PDB ID: 6W4H), clean it up, and prepare it for molecular dynamics simulations. Include proper protonation states and missing residues.
```

**The Structure Agent will create:**
- `structures/prepare_structure.py` - PDB processing and cleanup
- `structures/analyze_interface.py` - Interface analysis tools
- `structures/6w4h_processed.pdb` - Cleaned structure file

#### Agent 2: Simulation Setup and Execution

**Engage the Simulation Agent for MD setup:**
```
@agent:simulation Create OpenMM molecular dynamics simulation scripts for the Nsp10-Nsp16 complex. Include system setup with explicit water, energy minimization, equilibration, and production runs. Use AMBER force field.
```

**The Simulation Agent will create:**
- `simulations/setup_system.py` - OpenMM system preparation
- `simulations/run_simulation.py` - MD simulation execution
- `simulations/equilibration.py` - System equilibration protocol
- `simulations/production.py` - Production run management

#### Agent 3: Analysis and Visualization

**Deploy the Analysis Agent for data processing:**
```
@agent:analysis Create comprehensive analysis scripts for MD trajectory data. Include RMSD, RMSF, hydrogen bond analysis, contact maps, and binding free energy calculations using MDTraj and custom analysis tools.
```

**The Analysis Agent will create:**
- `analysis/trajectory_analysis.py` - Basic trajectory metrics
- `analysis/binding_analysis.py` - Protein-protein interaction analysis
- `analysis/energy_analysis.py` - Free energy calculations
- `analysis/visualization.py` - Interactive plots and 3D structures

#### Agent 4: Results Integration and Reporting

**Use the Reporting Agent for scientific documentation:**
```
@agent:reporting Create automated report generation scripts that compile simulation results, generate publication-quality figures, and create interactive notebooks for hypothesis validation.
```

### Detailed Implementation

Let's build this step-by-step with working code:

#### Step 1: Structure Preparation

```warp-runnable-command
# Ask the structure agent to create the preparation script
cat > structures/prepare_structure.py << 'EOF'
#!/usr/bin/env python3
"""
Structure Preparation for Nsp10-Nsp16 Complex
Prepares PDB structure for molecular dynamics simulations
"""

import requests
import os
from pdbfixer import PDBFixer
from openmm.app import PDBFile
import biotite.structure as struc
import biotite.structure.io as strucio
from biotite.structure.io.pdb import PDBFile as BiotitePDBFile

def download_structure(pdb_id="6W4H", output_dir="."):
    """Download PDB structure from RCSB"""
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    response = requests.get(url)
    
    if response.status_code == 200:
        filename = os.path.join(output_dir, f"{pdb_id.lower()}_raw.pdb")
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"Downloaded {pdb_id} to {filename}")
        return filename
    else:
        raise Exception(f"Failed to download {pdb_id}")

def clean_structure(input_pdb, output_pdb):
    """Clean and prepare structure using PDBFixer"""
    fixer = PDBFixer(filename=input_pdb)
    
    # Find and add missing residues
    fixer.findMissingResidues()
    
    # Find and add missing atoms
    fixer.findMissingAtoms()
    fixer.addMissingAtoms()
    
    # Add missing hydrogens
    fixer.addMissingHydrogens(7.0)  # pH 7.0
    
    # Write cleaned structure
    PDBFile.writeFile(fixer.topology, fixer.positions, open(output_pdb, 'w'))
    print(f"Cleaned structure saved to {output_pdb}")
    
    return output_pdb

def analyze_complex(pdb_file):
    """Analyze the protein complex interface"""
    # Load structure with biotite
    pdb_file_obj = BiotitePDBFile.read(pdb_file)
    structure = pdb_file_obj.get_structure()
    
    # Separate chains (assuming Nsp10 and Nsp16 are different chains)
    chains = struc.get_chains(structure)
    print(f"Found chains: {list(chains)}")
    
    # Calculate interface residues (simplified)
    chain_a = structure[struc.filter_amino_acids(structure) & (struc.get_chain_id(structure) == 'A')]
    chain_b = structure[struc.filter_amino_acids(structure) & (struc.get_chain_id(structure) == 'B')]
    
    print(f"Chain A residues: {len(struc.get_residues(chain_a))}")
    print(f"Chain B residues: {len(struc.get_residues(chain_b))}")
    
    return structure

def main():
    """Main structure preparation workflow"""
    print("Starting structure preparation for Nsp10-Nsp16 complex...")
    
    # Download structure
    raw_pdb = download_structure("6W4H", ".")
    
    # Clean structure
    clean_pdb = clean_structure(raw_pdb, "6w4h_processed.pdb")
    
    # Analyze complex
    structure = analyze_complex(clean_pdb)
    
    print("Structure preparation complete!")
    return clean_pdb

if __name__ == "__main__":
    main()
EOF
```

#### Step 2: OpenMM Simulation Setup

```warp-runnable-command
# Create the simulation setup script
cat > simulations/setup_system.py << 'EOF'
#!/usr/bin/env python3
"""
OpenMM System Setup for Nsp10-Nsp16 Complex
Creates simulation system with explicit solvent
"""

import openmm as mm
import openmm.app as app
import openmm.unit as unit
import numpy as np
from sys import stdout

def setup_system(pdb_file, output_prefix="nsp10_nsp16"):
    """Setup OpenMM system for MD simulation"""
    
    print("Loading structure...")
    pdb = app.PDBFile(pdb_file)
    
    print("Creating force field...")
    forcefield = app.ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
    
    print("Adding solvent...")
    # Add water box with 1.0 nm padding
    modeller = app.Modeller(pdb.topology, pdb.positions)
    modeller.addSolvent(forcefield, padding=1.0*unit.nanometer)
    
    print(f"System has {modeller.topology.getNumAtoms()} atoms")
    
    print("Creating system...")
    system = forcefield.createSystem(
        modeller.topology,
        nonbondedMethod=app.PME,
        nonbondedCutoff=1.0*unit.nanometer,
        constraints=app.HBonds
    )
    
    # Add barostat for NPT ensemble
    barostat = mm.MonteCarloBarostat(1*unit.bar, 300*unit.kelvin)
    system.addForce(barostat)
    
    print("Setting up integrator...")
    integrator = mm.LangevinMiddleIntegrator(
        300*unit.kelvin,
        1/unit.picosecond,
        0.002*unit.picoseconds
    )
    
    # Save system state
    print("Saving system files...")
    with open(f"{output_prefix}_system.xml", 'w') as f:
        f.write(mm.XmlSerializer.serialize(system))
    
    with open(f"{output_prefix}_integrator.xml", 'w') as f:
        f.write(mm.XmlSerializer.serialize(integrator))
    
    app.PDBFile.writeFile(modeller.topology, modeller.positions, 
                         open(f"{output_prefix}_solvated.pdb", 'w'))
    
    print("System setup complete!")
    return system, integrator, modeller.topology, modeller.positions

def minimize_energy(system, integrator, topology, positions, output_prefix="nsp10_nsp16"):
    """Perform energy minimization"""
    print("Starting energy minimization...")
    
    simulation = app.Simulation(topology, system, integrator)
    simulation.context.setPositions(positions)
    
    # Report initial energy
    state = simulation.context.getState(getEnergy=True)
    print(f"Initial potential energy: {state.getPotentialEnergy()}")
    
    # Minimize
    simulation.minimizeEnergy(maxIterations=1000)
    
    # Report final energy
    state = simulation.context.getState(getEnergy=True, getPositions=True)
    print(f"Final potential energy: {state.getPotentialEnergy()}")
    
    # Save minimized structure
    app.PDBFile.writeFile(topology, state.getPositions(), 
                         open(f"{output_prefix}_minimized.pdb", 'w'))
    
    print("Energy minimization complete!")
    return state.getPositions()

def main():
    """Main system setup workflow"""
    pdb_file = "../structures/6w4h_processed.pdb"
    
    # Setup system
    system, integrator, topology, positions = setup_system(pdb_file)
    
    # Minimize energy
    min_positions = minimize_energy(system, integrator, topology, positions)
    
    print("System ready for simulation!")

if __name__ == "__main__":
    main()
EOF
```

#### Step 3: Production Simulation

```warp-runnable-command
# Create the production simulation script
cat > simulations/run_simulation.py << 'EOF'
#!/usr/bin/env python3
"""
Production MD Simulation for Nsp10-Nsp16 Complex
Runs molecular dynamics simulation with trajectory output
"""

import openmm as mm
import openmm.app as app
import openmm.unit as unit
from sys import stdout
import time

def run_equilibration(system_file, integrator_file, pdb_file, steps=50000):
    """Run equilibration simulation"""
    print("Starting equilibration...")
    
    # Load system components
    with open(system_file, 'r') as f:
        system = mm.XmlSerializer.deserialize(f.read())
    
    with open(integrator_file, 'r') as f:
        integrator = mm.XmlSerializer.deserialize(f.read())
    
    pdb = app.PDBFile(pdb_file)
    
    # Create simulation
    simulation = app.Simulation(pdb.topology, system, integrator)
    simulation.context.setPositions(pdb.positions)
    
    # Add reporters
    simulation.reporters.append(app.StateDataReporter(
        stdout, 1000, step=True, time=True, temperature=True, 
        potentialEnergy=True, kineticEnergy=True, totalEnergy=True,
        volume=True, density=True, speed=True
    ))
    
    # Run equilibration
    print(f"Running {steps} equilibration steps...")
    start_time = time.time()
    simulation.step(steps)
    end_time = time.time()
    
    print(f"Equilibration completed in {end_time - start_time:.2f} seconds")
    
    # Save equilibrated state
    state = simulation.context.getState(getPositions=True)
    app.PDBFile.writeFile(pdb.topology, state.getPositions(), 
                         open('equilibrated.pdb', 'w'))
    
    return simulation

def run_production(system_file, integrator_file, pdb_file, 
                  steps=1000000, output_freq=1000):
    """Run production simulation with trajectory output"""
    print("Starting production simulation...")
    
    # Load system components
    with open(system_file, 'r') as f:
        system = mm.XmlSerializer.deserialize(f.read())
    
    with open(integrator_file, 'r') as f:
        integrator = mm.XmlSerializer.deserialize(f.read())
    
    pdb = app.PDBFile(pdb_file)
    
    # Create simulation
    simulation = app.Simulation(pdb.topology, system, integrator)
    simulation.context.setPositions(pdb.positions)
    
    # Add reporters
    simulation.reporters.append(app.StateDataReporter(
        'production.log', output_freq, step=True, time=True, 
        temperature=True, potentialEnergy=True, kineticEnergy=True,
        totalEnergy=True, volume=True, density=True, speed=True
    ))
    
    simulation.reporters.append(app.DCDReporter(
        'trajectory.dcd', output_freq
    ))
    
    simulation.reporters.append(app.CheckpointReporter(
        'checkpoint.chk', output_freq*10
    ))
    
    # Run production
    print(f"Running {steps} production steps...")
    print(f"Trajectory will be saved every {output_freq} steps")
    
    start_time = time.time()
    simulation.step(steps)
    end_time = time.time()
    
    simulation_time = steps * 0.002 * unit.picoseconds
    print(f"Production completed in {end_time - start_time:.2f} seconds")
    print(f"Simulated {simulation_time} of molecular time")
    
    return simulation

def main():
    """Main simulation workflow"""
    # File paths
    system_file = "nsp10_nsp16_system.xml"
    integrator_file = "nsp10_nsp16_integrator.xml"
    pdb_file = "nsp10_nsp16_minimized.pdb"
    
    # Run equilibration (100 ps)
    equilibration_sim = run_equilibration(system_file, integrator_file, pdb_file, 50000)
    
    # Run production (2 ns)
    production_sim = run_production(system_file, integrator_file, 
                                   "equilibrated.pdb", 1000000, 1000)
    
    print("Simulation workflow complete!")
    print("Output files:")
    print("- trajectory.dcd: MD trajectory")
    print("- production.log: Simulation log")
    print("- checkpoint.chk: Restart checkpoint")

if __name__ == "__main__":
    main()
EOF
```

#### Step 4: Analysis Framework

```warp-runnable-command
# Create comprehensive analysis script
cat > analysis/trajectory_analysis.py << 'EOF'
#!/usr/bin/env python3
"""
MD Trajectory Analysis for Nsp10-Nsp16 Complex
Analyzes simulation data to validate hypothesis
"""

import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd

def load_trajectory(topology_file, trajectory_file):
    """Load MD trajectory"""
    print(f"Loading trajectory from {trajectory_file}...")
    traj = md.load(trajectory_file, top=topology_file)
    print(f"Trajectory: {traj.n_frames} frames, {traj.n_atoms} atoms")
    print(f"Time span: {traj.time[-1]:.2f} ps")
    return traj

def calculate_rmsd(traj, reference_frame=0):
    """Calculate RMSD relative to reference frame"""
    print("Calculating RMSD...")
    
    # Align trajectory
    traj.superpose(traj, frame=reference_frame)
    
    # Calculate RMSD
    rmsd = md.rmsd(traj, traj, frame=reference_frame) * 10  # Convert to Angstroms
    
    return rmsd

def calculate_rmsf(traj):
    """Calculate root mean square fluctuation per residue"""
    print("Calculating RMSF...")
    
    # Get protein atoms only
    protein_atoms = traj.topology.select('protein')
    protein_traj = traj.atom_slice(protein_atoms)
    
    # Align trajectory
    protein_traj.superpose(protein_traj, frame=0)
    
    # Calculate RMSF
    rmsf = np.sqrt(np.mean((protein_traj.xyz - protein_traj.xyz.mean(axis=0))**2, axis=0))
    rmsf = rmsf.mean(axis=1) * 10  # Convert to Angstroms, average over atoms per residue
    
    return rmsf

def analyze_hydrogen_bonds(traj, distance_cutoff=0.35, angle_cutoff=120):
    """Analyze hydrogen bonds at the interface"""
    print("Analyzing hydrogen bonds...")
    
    # Find potential hydrogen bond donors and acceptors
    hbonds = md.baker_hubbard(traj, freq=0.1, exclude_water=True)
    
    # Calculate hydrogen bond occupancy
    hbond_occupancy = {}
    for hbond in hbonds:
        donor_residue = traj.topology.atom(hbond[0]).residue
        acceptor_residue = traj.topology.atom(hbond[2]).residue
        
        bond_key = f"{donor_residue.name}{donor_residue.resSeq}-{acceptor_residue.name}{acceptor_residue.resSeq}"
        hbond_occupancy[bond_key] = hbond_occupancy.get(bond_key, 0) + 1
    
    # Convert to percentages
    for key in hbond_occupancy:
        hbond_occupancy[key] = (hbond_occupancy[key] / traj.n_frames) * 100
    
    return hbond_occupancy

def calculate_contact_map(traj, scheme='closest-heavy'):
    """Calculate residue contact map"""
    print("Calculating contact map...")
    
    # Calculate distances between all residue pairs
    distances, residue_pairs = md.compute_contacts(traj, scheme=scheme)
    
    # Average over time
    avg_distances = distances.mean(axis=0)
    
    return avg_distances, residue_pairs

def plot_analysis_results(time, rmsd, rmsf, hbond_occupancy):
    """Create analysis plots"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    
    # RMSD plot
    axes[0, 0].plot(time, rmsd, 'b-', alpha=0.7)
    axes[0, 0].set_xlabel('Time (ps)')
    axes[0, 0].set_ylabel('RMSD (Å)')
    axes[0, 0].set_title('RMSD vs Time')
    axes[0, 0].grid(True, alpha=0.3)
    
    # RMSF plot
    axes[0, 1].plot(range(len(rmsf)), rmsf, 'r-', alpha=0.7)
    axes[0, 1].set_xlabel('Residue Number')
    axes[0, 1].set_ylabel('RMSF (Å)')
    axes[0, 1].set_title('Root Mean Square Fluctuation')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Hydrogen bond occupancy
    if hbond_occupancy:
        bonds = list(hbond_occupancy.keys())[:10]  # Top 10 bonds
        occupancies = [hbond_occupancy[bond] for bond in bonds]
        
        axes[1, 0].barh(range(len(bonds)), occupancies)
        axes[1, 0].set_yticks(range(len(bonds)))
        axes[1, 0].set_yticklabels(bonds, fontsize=8)
        axes[1, 0].set_xlabel('Occupancy (%)')
        axes[1, 0].set_title('Top Hydrogen Bonds')
    
    # RMSD distribution
    axes[1, 1].hist(rmsd, bins=30, alpha=0.7, density=True)
    axes[1, 1].set_xlabel('RMSD (Å)')
    axes[1, 1].set_ylabel('Probability Density')
    axes[1, 1].set_title('RMSD Distribution')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('trajectory_analysis.png', dpi=300, bbox_inches='tight')
    plt.show()

def generate_summary_report(rmsd, rmsf, hbond_occupancy, simulation_time):
    """Generate analysis summary"""
    print("\n" + "="*50)
    print("SIMULATION ANALYSIS SUMMARY")
    print("="*50)
    
    print(f"Simulation Time: {simulation_time:.2f} ps")
    print(f"Number of Frames: {len(rmsd)}")
    
    print("\nStructural Stability:")
    print(f"  Average RMSD: {rmsd.mean():.2f} ± {rmsd.std():.2f} Å")
    print(f"  Maximum RMSD: {rmsd.max():.2f} Å")
    print(f"  Final RMSD: {rmsd[-1]:.2f} Å")
    
    print(f"\nFlexibility (RMSF):")
    print(f"  Average RMSF: {rmsf.mean():.2f} ± {rmsf.std():.2f} Å")
    print(f"  Most flexible residue: {rmsf.argmax()} (RMSF: {rmsf.max():.2f} Å)")
    print(f"  Most rigid residue: {rmsf.argmin()} (RMSF: {rmsf.min():.2f} Å)")
    
    if hbond_occupancy:
        print(f"\nHydrogen Bonding:")
        print(f"  Total unique H-bonds: {len(hbond_occupancy)}")
        top_hbond = max(hbond_occupancy.items(), key=lambda x: x[1])
        print(f"  Most stable H-bond: {top_hbond[0]} ({top_hbond[1]:.1f}% occupancy)")
    
    print("\nHypothesis Validation:")
    if rmsd.mean() < 3.0:
        print("  ✓ Complex shows good structural stability (RMSD < 3 Å)")
    else:
        print("  ✗ Complex shows significant structural drift")
    
    if len([occ for occ in hbond_occupancy.values() if occ > 50]) > 0:
        print("  ✓ Stable hydrogen bonds detected at interface")
    else:
        print("  ? Few stable hydrogen bonds detected")
    
    print("="*50)

def main():
    """Main analysis workflow"""
    # Load trajectory
    topology_file = "../simulations/nsp10_nsp16_solvated.pdb"
    trajectory_file = "../simulations/trajectory.dcd"
    
    traj = load_trajectory(topology_file, trajectory_file)
    
    # Perform analyses
    rmsd = calculate_rmsd(traj)
    rmsf = calculate_rmsf(traj)
    hbond_occupancy = analyze_hydrogen_bonds(traj)
    
    # Create plots
    plot_analysis_results(traj.time, rmsd, rmsf, hbond_occupancy)
    
    # Generate summary
    generate_summary_report(rmsd, rmsf, hbond_occupancy, traj.time[-1])
    
    # Save data
    results = {
        'time': traj.time,
        'rmsd': rmsd,
        'rmsf': rmsf,
        'hbond_occupancy': hbond_occupancy
    }
    
    np.savez('analysis_results.npz', **{k: v for k, v in results.items() if k != 'hbond_occupancy'})
    
    print("\nAnalysis complete! Results saved to analysis_results.npz")
    return results

if __name__ == "__main__":
    main()
EOF
```

### Multi-Agent Coordination for Computational Workflows

#### Coordinated Execution Pipeline

```warp-runnable-command
# Create a master coordination script
cat > run_computational_pipeline.py << 'EOF'
#!/usr/bin/env python3
"""
Master Pipeline for Nsp10-Nsp16 Computational Study
Coordinates multi-agent workflow for hypothesis validation
"""

import subprocess
import sys
import os
import time
from pathlib import Path

def run_agent_task(agent_name, task_description, script_path):
    """Execute agent task with error handling"""
    print(f"\n{'='*60}")
    print(f"AGENT: {agent_name.upper()}")
    print(f"TASK: {task_description}")
    print(f"{'='*60}")
    
    if not os.path.exists(script_path):
        print(f"ERROR: Script {script_path} not found!")
        return False
    
    try:
        start_time = time.time()
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, text=True, check=True)
        end_time = time.time()
        
        print(f"SUCCESS: Task completed in {end_time - start_time:.2f} seconds")
        if result.stdout:
            print("Output:")
            print(result.stdout)
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Task failed with return code {e.returncode}")
        if e.stderr:
            print("Error output:")
            print(e.stderr)
        return False

def main():
    """Execute complete computational pipeline"""
    print("Starting Nsp10-Nsp16 Computational Study Pipeline")
    print("Hypothesis: Nsp10-Nsp16 binding involves stable H-bonds and hydrophobic interactions")
    
    # Define pipeline stages
    pipeline = [
        ("Structure Agent", "Prepare and analyze protein complex structure", "structures/prepare_structure.py"),
        ("Simulation Agent", "Setup molecular dynamics system", "simulations/setup_system.py"),
        ("Execution Agent", "Run production simulation", "simulations/run_simulation.py"),
        ("Analysis Agent", "Analyze trajectory and validate hypothesis", "analysis/trajectory_analysis.py")
    ]
    
    # Execute pipeline
    results = []
    for agent_name, task_description, script_path in pipeline:
        success = run_agent_task(agent_name, task_description, script_path)
        results.append((agent_name, success))
        
        if not success:
            print(f"\nPipeline failed at {agent_name} stage")
            break
    
    # Summary
    print(f"\n{'='*60}")
    print("PIPELINE SUMMARY")
    print(f"{'='*60}")
    
    for agent_name, success in results:
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{agent_name}: {status}")
    
    if all(success for _, success in results):
        print("\n🎉 Complete computational workflow successful!")
        print("\nNext steps:")
        print("1. Review analysis results in analysis_results.npz")
        print("2. Examine trajectory_analysis.png for visualizations")
        print("3. Consider extended simulations or parameter variations")
    else:
        print("\n❌ Pipeline incomplete - check error messages above")

if __name__ == "__main__":
    main()
EOF
```

### Interactive Computational Notebook

**Ask the Documentation Agent to create an interactive notebook:**
```
@agent:documentation Create a Jupyter notebook that combines all the computational biology workflow steps with interactive visualizations, hypothesis tracking, and results interpretation for the Nsp10-Nsp16 study.
```

### Advanced Multi-Agent Computational Patterns

#### Pattern 1: Parallel Parameter Studies

```
# Different agents handle different simulation conditions
@agent:sim_300K Run simulation at 300K temperature
@agent:sim_310K Run simulation at 310K temperature (fever conditions)
@agent:sim_280K Run simulation at 280K temperature (hypothermia)

# Analysis agent compares all conditions
@agent:comparative_analysis Compare binding stability across different temperature conditions
```

#### Pattern 2: Multi-Scale Modeling

```
# Coarse-grained agent for long timescales
@agent:cg_simulation Run coarse-grained simulation for microsecond timescales

# Atomistic agent for detailed interactions
@agent:atomistic_simulation Run all-atom simulation for detailed binding analysis

# Integration agent combines insights
@agent:multiscale_integration Combine CG and atomistic results for complete picture
```

#### Pattern 3: Machine Learning Integration

```
# ML agent for pattern recognition
@agent:ml_analysis Use machine learning to identify key binding residues from simulation data

# Prediction agent for drug design
@agent:drug_prediction Predict potential drug binding sites based on simulation analysis
```

### Running the Complete Computational Workflow

```warp-runnable-command
# Execute the complete pipeline
python run_computational_pipeline.py
```

### Hypothesis Validation Framework

**Track hypothesis validation throughout the workflow:**

```warp-runnable-command
cat > hypothesis_tracker.py << 'EOF'
#!/usr/bin/env python3
"""
Hypothesis Validation Tracker
Tracks and validates scientific hypotheses throughout computational workflow
"""

import json
from datetime import datetime

class HypothesisTracker:
    def __init__(self, hypothesis_file="hypothesis_log.json"):
        self.hypothesis_file = hypothesis_file
        self.load_hypotheses()
    
    def load_hypotheses(self):
        try:
            with open(self.hypothesis_file, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {"hypotheses": [], "validations": []}
    
    def save_hypotheses(self):
        with open(self.hypothesis_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_hypothesis(self, hypothesis, rationale, testable_predictions):
        """Add a new hypothesis to track"""
        new_hypothesis = {
            "id": len(self.data["hypotheses"]) + 1,
            "hypothesis": hypothesis,
            "rationale": rationale,
            "predictions": testable_predictions,
            "timestamp": datetime.now().isoformat(),
            "status": "pending"
        }
        self.data["hypotheses"].append(new_hypothesis)
        self.save_hypotheses()
        return new_hypothesis["id"]
    
    def validate_hypothesis(self, hypothesis_id, results, validation_status):
        """Validate hypothesis based on computational results"""
        validation = {
            "hypothesis_id": hypothesis_id,
            "results": results,
            "status": validation_status,  # "supported", "rejected", "inconclusive"
            "timestamp": datetime.now().isoformat()
        }
        self.data["validations"].append(validation)
        
        # Update hypothesis status
        for hyp in self.data["hypotheses"]:
            if hyp["id"] == hypothesis_id:
                hyp["status"] = validation_status
                break
        
        self.save_hypotheses()
    
    def generate_report(self):
        """Generate hypothesis validation report"""
        print("HYPOTHESIS VALIDATION REPORT")
        print("=" * 50)
        
        for hyp in self.data["hypotheses"]:
            print(f"\nHypothesis {hyp['id']}: {hyp['status'].upper()}")
            print(f"Statement: {hyp['hypothesis']}")
            print(f"Rationale: {hyp['rationale']}")
            
            # Find validations for this hypothesis
            validations = [v for v in self.data["validations"] if v["hypothesis_id"] == hyp["id"]]
            if validations:
                latest = validations[-1]
                print(f"Latest validation: {latest['status']}")
                print(f"Evidence: {latest['results']}")

# Example usage
if __name__ == "__main__":
    tracker = HypothesisTracker()
    
    # Add main hypothesis
    hyp_id = tracker.add_hypothesis(
        "The Nsp10-Nsp16 complex is stabilized by specific hydrogen bonds and hydrophobic interactions",
        "Structural analysis suggests key interface residues form stable interactions",
        ["RMSD < 3Å during simulation", "H-bond occupancy > 50% for key residues", "Stable contact map"]
    )
    
    print(f"Tracking hypothesis {hyp_id}")
    tracker.generate_report()
EOF
```

### Performance Monitoring for Computational Workflows

```warp-runnable-command
# Create performance monitoring script
cat > monitor_performance.py << 'EOF'
#!/usr/bin/env python3
"""
Performance Monitor for Computational Workflows
Tracks resource usage and optimization opportunities
"""

import psutil
import time
import matplotlib.pyplot as plt
from threading import Thread
import json

class PerformanceMonitor:
    def __init__(self):
        self.monitoring = False
        self.data = {"time": [], "cpu": [], "memory": [], "disk_io": []}
    
    def start_monitoring(self, interval=5):
        """Start performance monitoring"""
        self.monitoring = True
        self.monitor_thread = Thread(target=self._monitor_loop, args=(interval,))
        self.monitor_thread.start()
    
    def stop_monitoring(self):
        """Stop performance monitoring"""
        self.monitoring = False
        self.monitor_thread.join()
    
    def _monitor_loop(self, interval):
        """Monitor system performance"""
        start_time = time.time()
        
        while self.monitoring:
            current_time = time.time() - start_time
            cpu_percent = psutil.cpu_percent()
            memory_percent = psutil.virtual_memory().percent
            disk_io = psutil.disk_io_counters()
            
            self.data["time"].append(current_time)
            self.data["cpu"].append(cpu_percent)
            self.data["memory"].append(memory_percent)
            self.data["disk_io"].append(disk_io.read_bytes + disk_io.write_bytes)
            
            time.sleep(interval)
    
    def plot_performance(self):
        """Plot performance metrics"""
        fig, axes = plt.subplots(3, 1, figsize=(12, 10))
        
        axes[0].plot(self.data["time"], self.data["cpu"])
        axes[0].set_ylabel("CPU Usage (%)")
        axes[0].set_title("System Performance During Simulation")
        axes[0].grid(True)
        
        axes[1].plot(self.data["time"], self.data["memory"])
        axes[1].set_ylabel("Memory Usage (%)")
        axes[1].grid(True)
        
        disk_gb = [x / (1024**3) for x in self.data["disk_io"]]
        axes[2].plot(self.data["time"], disk_gb)
        axes[2].set_ylabel("Cumulative Disk I/O (GB)")
        axes[2].set_xlabel("Time (seconds)")
        axes[2].grid(True)
        
        plt.tight_layout()
        plt.savefig("performance_monitor.png", dpi=300)
        plt.show()
    
    def save_data(self, filename="performance_data.json"):
        """Save performance data"""
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)

# Example usage for monitoring MD simulations
if __name__ == "__main__":
    monitor = PerformanceMonitor()
    
    print("Starting performance monitoring...")
    monitor.start_monitoring(interval=10)
    
    # Simulate some work (replace with actual simulation)
    print("Running simulation... (this is a demo)")
    time.sleep(60)  # Monitor for 1 minute
    
    monitor.stop_monitoring()
    monitor.plot_performance()
    monitor.save_data()
    
    print("Performance monitoring complete!")
EOF
```

This comprehensive computational biology section demonstrates:

- **Real scientific workflow** with hypothesis-driven research
- **Multi-agent coordination** for complex computational tasks
- **Professional molecular dynamics** simulation setup with OpenMM
- **Comprehensive analysis** including RMSD, RMSF, hydrogen bonds
- **Performance monitoring** for resource optimization
- **Hypothesis validation framework** for scientific rigor
- **Automated pipeline execution** with error handling
- **Interactive notebooks** for collaborative research

The workflow is designed to be both educational and practical, showing how Warp can handle real computational science workflows while teaching important concepts in molecular dynamics and scientific computing.

---

## Part 10: Notebook Integration

Warp's Notebook feature allows you to create interactive, executable documentation. This tutorial itself is an example of a notebook!

### Creating Your Own Notebook

1. Save this file as a `.md` file
2. Open it in Warp
3. Use the `warp-runnable-command` blocks to make commands executable
4. Share with your team for collaborative development

### Best Practices for Notebooks

- Use clear section headers
- Include explanatory text between code blocks
- Add parameter placeholders with `{{parameter_name}}`
- Document expected outputs

---

## Part 10: Troubleshooting Common Issues

### Python Environment Issues

```warp-runnable-command
which python
```

```warp-runnable-command
pip list
```

**If you have issues, ask:**
```
@agent Help me troubleshoot Python environment issues - I'm getting import errors
```

### Package Installation Problems

```warp-runnable-command
pip install --upgrade pip
```

**For complex dependency issues:**
```
@agent Help me resolve package dependency conflicts in my Python project
```

---

## Part 11: Next Steps and Advanced Topics

### Explore More AI Capabilities

Try asking the agent to help with:
- Creating unit tests for existing code
- Optimizing slow Python code
- Converting scripts to object-oriented design
- Adding logging and configuration management
- Creating command-line interfaces with argparse or click

### Integration with Development Tools

```warp-runnable-command
pip install jupyter ipython
```

**Ask the agent:**
```
@agent Show me how to integrate Jupyter notebooks with my Python development workflow
```

### Deployment and Distribution

**Ask the agent:**
```
@agent Help me create a setup.py file and package my Python project for distribution
```

---

## Conclusion

This tutorial has demonstrated the key capabilities of Warp for Python development:

✅ **Agentic Coding**: AI writes complete, functional code based on natural language descriptions
✅ **Interactive Development**: Smart suggestions and real-time assistance
✅ **Debugging**: AI-powered error resolution and code improvement
✅ **Testing**: Automated test creation and execution
✅ **Workflows**: Streamlined development processes
✅ **Notebooks**: Interactive, shareable documentation

### Key Takeaways

1. **Start with natural language**: Describe what you want to build, and let AI create the initial code
2. **Iterate and improve**: Use AI to refine, debug, and enhance your code
3. **Learn by doing**: Even as a beginner, you can build complex applications with AI assistance
4. **Document everything**: Use notebooks to create shareable, executable documentation
5. **Automate repetitive tasks**: Let Warp handle routine development workflows

### What's Next?

- Try building your own project using these techniques
- Explore Warp's integration with version control systems
- Create your own automation scripts and workflows
- Share your notebooks with teammates for collaborative development

Remember: The best way to learn is by experimenting. Don't hesitate to ask Warp's AI Agent for help with any coding challenge you encounter!

---

## Resources

- [Warp Documentation](https://docs.warp.dev/)
- [Python Official Documentation](https://docs.python.org/)
- [Python Package Index (PyPI)](https://pypi.org/)

Happy coding with Warp! 🚀
