/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let graph = Array.from({ length: numCourses }, () => []);
    let visited = Array(numCourses).fill(false);

    for(let [a, b] of prerequisites){
        graph[b].push(a);
    }

    const dfs = (node, path = []) => {
        if (path.includes(node)) return false;
        if (visited[node]) return true;

        visited[node] = true;
        path.push(node);
        for(let v of graph[node]){
            if(!dfs(v, path)){
                return false;
            }
        }
        path.pop();
        return true;
    }
    
    for(let node = 0; node < numCourses; node++){
        if(!visited[node]){
            if(!dfs(node)){
                return false;
            }
        }
    }

    return true;
};