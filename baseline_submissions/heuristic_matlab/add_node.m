function [nodes,filtered] = add_node(n, nodes, longitudes, inclinations, filtered)
    nodes{end} = nodes{end}.char_mode(n.index, longitudes, inclinations);

    if strcmp(n.type, 'AD')
        nodes{end}.mtype = 'NK';
    end

    if ~strcmp(nodes{end}.mtype, 'NK')
        filtered.indices = [filtered.indices; nodes{end}.index, n.index];
        filtered.modes.SK = [filtered.modes.SK; nodes{end}.mtype];
        stop_NS = strcmp(n.type, 'ID');
        filtered.modes.end = [filtered.modes.end; stop_NS];
    end
    
    nodes{end+1} = n;
end