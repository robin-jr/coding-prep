package main

import "fmt"

type Dep struct {
	Prereq int
	Job    int
}

func TopologicalSort(jobs []int, deps []Dep) []int {
	g := NewGraph(jobs, deps)
	finalOrder := []int{}
	for _, job := range jobs {
		hasCycle := dfs(g, job, &finalOrder)
		if hasCycle {
			return []int{}
		}
	}
	return finalOrder
}

func dfs(g *Graph, job int, finalOrder *[]int) bool {
	currJob := g.jobs[job]
	if currJob.visited {
		return false
	}
	if currJob.visiting {
		return true
	}
	currJob.visiting = true
	g.jobs[job] = currJob
	for _, prereq := range currJob.prereqs {
		hasCycle := dfs(g, prereq, finalOrder)
		if hasCycle {
			return true
		}
	}
	(*finalOrder) = append((*finalOrder), job)
	currJob.visited = true
	currJob.visiting = true
	g.jobs[job] = currJob
	return false
}

type Graph struct {
	jobs map[int]JobNode
}

func NewGraph(jobs []int, deps []Dep) *Graph {
	g := &Graph{jobs: make(map[int]JobNode)}
	for _, job := range jobs {
		g.jobs[job] = JobNode{job: job}
	}
	for _, dep := range deps {
		prereq, job := g.jobs[dep.Prereq], g.jobs[dep.Job]
		job.addPrereq(&prereq)
		g.jobs[dep.Job] = job
	}
	return g
}

type JobNode struct {
	job               int
	prereqs           []int
	visited, visiting bool
}

func (j *JobNode) addPrereq(t *JobNode) {
	j.prereqs = append(j.prereqs, t.job)
}

func main() {
	jobs := []int{1, 2, 3, 4}
	deps := []Dep{
		{1, 2},
		{1, 3},
		{3, 2},
		{4, 2},
		{4, 3},
	}
	x := TopologicalSort(jobs, deps)
	fmt.Println(x)
}
