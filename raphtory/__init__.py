from datetime import datetime
from typing import (
    Any,
    Callable,
    Iterator,
    Optional,
    Union,
)

import networkx as nx
import pandas as pd

# TODO: Edges, Nodes, TemporalProperties


class VectorisedGraph:
    ...


class GraphIndex:
    ...


class Properties:
    """A view of the properties of an entity"""

    @property
    def constant(self) -> "Properties":
        """Get a view of the constant properties (meta-data) only."""
        ...

    @property
    def temporal(self) -> "Properties":
        """Get a view of the temporal properties only."""
        ...

    def as_dict(self) -> dict[str, Any]:
        """Convert properties view to a dict"""
        ...

    def get(self, key: str) -> Any:
        """
        Get property value.
        First searches temporal properties and returns latest value if it exists.
        If not, it falls back to static properties.
        """
        ...

    def items(self) -> list[tuple[str, Any]]:
        """Get a list of key-value pairs"""
        ...

    def keys(self) -> list[str]:
        """Get the names for all properties (includes temporal and static properties)"""
        ...

    def values(self) -> list[Any]:
        """
        Get the values of the properties
        If a property exists as both temporal and static, temporal properties take priority
        with fallback to the static property if the temporal value does not exist.
        """
        ...


class ConstProperties:
    """A view of constant properties of an entity"""

    def as_dict(self) -> dict[str, Any]:
        """Convert the properties view to a python dict"""
        ...

    def get(self, key: str) -> Optional[Any]:
        """
        Get property value by key (returns None if key does not exist)

        Parameters:
        key (str): The name of the property

        Returns:
        Optional[Any]: The value of the property, or None if it doesn't exist
        """
        ...

    def items(self) -> list[tuple[str, Any]]:
        """Lists the property keys together with the corresponding value"""
        ...

    def keys(self) -> list[str]:
        """Lists the available property keys"""
        ...

    def values(self) -> list[Any]:
        """Lists the property values"""
        ...


class WindowSet:
    ...


class Node:
    def after(self, start: Union[int, datetime, str]) -> "Node":
        """Create a view of the Node including all events after start (exclusive)."""
        ...

    def at(self, time: Union[int, datetime, str]) -> "Node":
        """Create a view of the Node including all events at time."""
        ...

    def before(self, end: Union[int, datetime, str]) -> "Node":
        """Create a view of the Node including all events before end (exclusive)."""
        ...

    def default_layer(self) -> "Node":
        """Return a view of Node containing only the default edge layer.

        :returns: The layered view
        :rtype: Node
        """
        ...

    def degree(self) -> int:
        """Get the degree of this node (i.e., the number of edges that are incident to it)."""
        ...

    @property
    def earliest_date_time(self) -> datetime:
        """Returns the earliest datetime that the node exists."""
        ...

    @property
    def earliest_time(self) -> int:
        """Returns the earliest time that the node exists."""
        ...

    def edges(self) -> Iterator["Edge"]:
        """Get the edges that are incident to this node."""
        ...

    @property
    def end(self) -> Optional[int]:
        """Gets the latest time that this Node is valid."""
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        """Gets the latest datetime that this Node is valid."""
        ...

    def exclude_layer(self, name: str) -> "Node":
        """Return a view of Node containing all layers except the excluded name.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_layers(self, names: list[str]) -> "Node":
        """Return a view of Node containing all layers except the excluded names.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_valid_layer(self, name: str) -> "Node":
        """Return a view of Node containing all layers except the excluded name.

        :param name: Layer name that is excluded for the new view
        :type name: str
        """
        ...

    def exclude_valid_layers(self, names: list[str]) -> "Node":
        """Return a view of Node containing all layers except the excluded names.

        :param names: List of layer names that are excluded for the new view
        :type names: list[str]
        """
        ...

    def expanding(self, step: Union[int, str]) -> "WindowSet":
        """Creates a WindowSet with the given step size using an expanding window."""
        ...

    def has_layer(self, name: str) -> bool:
        """Check if Node has the layer 'name'."""
        ...

    def history(self) -> list[int]:
        """Returns the history of a node, including node additions and changes made to node."""
        ...

    def history_date_time(self) -> list[datetime]:
        """Returns the history of a node, including node additions and changes made to node."""
        ...

    @property
    def id(self) -> int:
        """Returns the id of the node."""
        ...

    def in_degree(self) -> int:
        """Get the in-degree of this node (i.e., the number of edges that are incident to it from other nodes)."""
        ...

    @property
    def in_edges(self) -> Iterator["Edge"]:
        """Get the edges that point into this node."""
        ...

    @property
    def in_neighbours(self) -> Iterator["Node"]:
        """Get the neighbours of this node that point into this node."""
        ...

    @property
    def latest_date_time(self) -> datetime:
        """Returns the latest datetime that the node exists."""
        ...

    @property
    def latest_time(self) -> int:
        """Returns the latest time that the node exists."""
        ...

    def layer(self, name: str) -> "Node":
        """Return a view of Node containing the layer 'name'.

        Errors if the layer does not exist.
        """
        ...

    def layers(self, names: list[str]) -> "Node":
        """Return a view of Node containing all layers names.

        Errors if any of the layers do not exist.
        """
        ...

    @property
    def name(self) -> str:
        """Returns the name of the node."""
        ...

    @property
    def neighbours(self) -> Iterator["Node"]:
        """Get the neighbours of this node."""
        ...

    @property
    def node_type(self) -> Optional[str]:
        """Returns the type of node."""
        ...

    def out_degree(self) -> int:
        """Get the out-degree of this node (i.e., the number of edges that are incident to it from this node)."""
        ...

    @property
    def out_edges(self) -> Iterator["Edge"]:
        """Get the edges that point out of this node."""
        ...

    @property
    def out_neighbours(self) -> Iterator["Node"]:
        """Get the neighbours of this node that point out of this node."""
        ...

    @property
    def properties(self) -> "Properties":
        """The properties of the node."""
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> "WindowSet":
        """Creates a WindowSet with the given window size and optional step using a rolling window."""
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "Node":
        """Set the end of the window to the smaller of end and self.end()."""
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "Node":
        """Set the start of the window to the larger of start and self.start()."""
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "Node":
        """Shrink both the start and end of the window.

        Same as calling shrink_start followed by shrink_end but more efficient.
        """
        ...

    @property
    def start(self) -> Optional[int]:
        """Gets the start time for rolling and expanding windows for this Node."""
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        """Gets the earliest datetime that this Node is valid."""
        ...

    def valid_layers(self, names: list[str]) -> "Node":
        """Return a view of Node containing all layers names.

        Any layers that do not exist are ignored.
        """
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]] = None,
        end: Optional[Union[int, datetime, str]] = None,
    ) -> "Node":
        """Create a view of the Node including all events between start (inclusive) and end (exclusive)."""
        ...

    @property
    def window_size(self) -> Optional[int]:
        """Get the window size (difference between start and end) for this Node."""
        ...


class MutableNode(Node):
    def add_constant_properties(
        self, properties: dict[str, Any]
    ) -> None:  # TODO: Return Result object
        """Add constant properties to a node in the graph."""
        ...

    def add_updates(
        self,
        t: Union[int, str, datetime],
        properties: Optional[dict[str, Any]] = None,  # TODO: Return Result object
    ) -> None:
        """Add updates to a node in the graph at a specified time."""
        ...

    def set_node_type(self, properties: dict[str, Any]) -> None:
        """Add constant properties to a node in the graph."""
        ...

    def update_constant_properties(self, properties: dict[str, Any]) -> None:
        """Update constant properties of a node in the graph."""
        ...


class Edge:
    """Represents an edge in the graph. An edge is a directed connection between two nodes."""

    def after(self, start: Union[int, datetime, str]) -> "Edge":
        """Create a view of the Edge including all events after start (exclusive)."""
        ...

    def at(self, time: Union[int, datetime, str]) -> "Edge":
        """Create a view of the Edge including all events at time."""
        ...

    def before(self, end: Union[int, datetime, str]) -> "Edge":
        """Create a view of the Edge including all events before end (exclusive)."""
        ...

    @property
    def date_time(self) -> datetime:
        """Gets the datetime of an exploded edge."""
        ...

    def default_layer(self) -> "Edge":
        """Return a view of Edge containing only the default edge layer.

        :returns: The layered view
        :rtype: Edge
        """
        ...

    def deletions(self) -> list[int]:
        """Returns a list of timestamps of when an edge is deleted."""
        ...

    def deletions_data_time(self) -> list[datetime]:
        """Returns a list of timestamps of when an edge is deleted."""
        ...

    @property
    def dst(self) -> "Node":
        """Returns the destination node of the edge."""
        ...

    @property
    def earliest_date_time(self) -> datetime:
        """Gets the earliest datetime of an edge."""
        ...

    @property
    def earliest_time(self) -> int:
        """Gets the earliest time of an edge."""
        ...

    @property
    def end(self) -> Optional[int]:
        """Gets the latest time that this Edge is valid."""
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        """Gets the latest datetime that this Edge is valid."""
        ...

    def exclude_layer(self, name: str) -> "Edge":
        """Return a view of Edge containing all layers except the excluded name.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_layers(self, names: list[str]) -> "Edge":
        """Return a view of Edge containing all layers except the excluded names.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_valid_layer(self, name: str) -> "Edge":
        """Return a view of Edge containing all layers except the excluded name.

        :param name: Layer name that is excluded for the new view
        :type name: str
        """
        ...

    def exclude_valid_layers(self, names: list[str]) -> "Edge":
        """Return a view of Edge containing all layers except the excluded names.

        :param names: List of layer names that are excluded for the new view
        :type names: list[str]
        """
        ...

    def expanding(self, step: Union[int, str]) -> "WindowSet":
        """Creates a WindowSet with the given step size using an expanding window."""
        ...

    def explode(self) -> list["Edge"]:
        """Explodes an edge and returns all instances it had been updated as separate edges."""
        ...

    def explode_layers(self) -> list["Edge"]:
        """Explode the edge into its constituent layers."""
        ...

    def has_layer(self, name: str) -> bool:
        """Check if Edge has the layer 'name'."""
        ...

    def history(self) -> list[int]:
        """Returns a list of timestamps of when an edge is added or a change to an edge is made."""
        ...

    def history_date_time(self) -> list[datetime]:
        """Returns a list of timestamps of when an edge is added or a change to an edge is made."""
        ...

    @property
    def id(self) -> Union[int, str]:
        """The id of the edge."""
        ...

    def is_deleted(self) -> bool:
        """Check if the edge is currently deleted."""
        ...

    def is_self_loop(self) -> bool:
        """Check if the edge is on the same node."""
        ...

    def is_valid(self) -> bool:
        """Check if the edge is currently valid (i.e., not deleted)."""
        ...

    @property
    def latest_date_time(self) -> datetime:
        """Gets the latest datetime of an edge."""
        ...

    @property
    def latest_time(self) -> int:
        """Gets the latest time of an edge."""
        ...

    def layer(self, name: str) -> "Edge":
        """Return a view of Edge containing the layer 'name'.

        Errors if the layer does not exist.
        """
        ...

    @property
    def layer_name(self) -> str:
        """Gets the name of the layer this edge belongs to, assuming it only belongs to one layer."""
        ...

    @property
    def layer_names(self) -> list[str]:
        """Gets the names of the layers this edge belongs to."""
        ...

    def layers(self, names: list[str]) -> "Edge":
        """Return a view of Edge containing all layers names.

        Errors if any of the layers do not exist.
        """
        ...

    @property
    def nbr(self) -> "Node":
        """Returns the node at the other end of the edge (same as dst() for out-edges and src() for in-edges)."""
        ...

    @property
    def properties(self) -> dict[str, Any]:
        """Returns a view of the properties of the edge."""
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> "WindowSet":
        """Creates a WindowSet with the given window size and optional step using a rolling window."""
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "Edge":
        """Set the end of the window to the smaller of end and self.end()."""
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "Edge":
        """Set the start of the window to the larger of start and self.start()."""
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "Edge":
        """Shrink both the start and end of the window.

        Same as calling shrink_start followed by shrink_end but more efficient.
        """
        ...

    @property
    def src(self) -> "Node":
        """Returns the source node of the edge."""
        ...

    @property
    def start(self) -> Optional[int]:
        """Gets the start time for rolling and expanding windows for this Edge."""
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        """Gets the earliest datetime that this Edge is valid."""
        ...

    @property
    def time(self) -> int:
        """Gets the time of an exploded edge."""
        ...

    def valid_layers(self, names: list[str]) -> "Edge":
        """Return a view of Edge containing all layers names.

        Any layers that do not exist are ignored.
        """
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]],
        end: Optional[Union[int, datetime, str]],
    ) -> "Edge":
        """Create a view of the Edge including all events between start (inclusive) and end (exclusive)."""
        ...

    @property
    def window_size(self) -> Optional[int]:
        """Get the window size (difference between start and end) for this Edge."""
        ...


class MutableEdge(Edge):
    def add_constant_properties(
        self, properties: dict[str, Any], layer: Optional[str] = None
    ) -> None:  # TODO: Return Result object
        """Add constant properties to an edge in the graph."""
        ...

    def add_updates(
        self,
        t: Union[int, str, datetime],
        properties: Optional[dict[str, Any]] = None,
        layer: Optional[str] = None,
    ) -> None:  # TODO: Return Result object
        """Add updates to an edge in the graph at a specified time."""
        ...

    def update_constant_properties(
        self, properties: dict[str, Any], layer: Optional[str] = None
    ) -> None:
        """Update constant properties of an edge in the graph."""
        ...


class GraphView:
    def add_constant_properties(self, properties: dict[str, Any]) -> None:
        """Adds static properties to the graph."""
        ...

    def add_edge(
        self,
        timestamp: Union[int, str, datetime],
        src: Union[str, int],
        dst: Union[str, int],
        properties: Optional[dict[str, Any]] = None,
        layer: Optional[str] = None,
    ) -> None:
        """Adds a new edge with the given source and destination nodes and properties to the graph."""
        ...

    def add_node(
        self,
        timestamp: Union[int, str, datetime],
        id: Union[str, int],
        properties: Optional[dict[str, Any]] = None,
        node_type: Optional[str] = None,
    ) -> None:
        """Adds a new node with the given id and properties to the graph."""
        ...

    def add_property(
        self, timestamp: Union[int, str, datetime], properties: dict[str, Any]
    ) -> None:
        """Adds properties to the graph."""
        ...

    def after(self, start: Union[int, datetime, str]) -> "GraphView":
        """Create a view of the GraphView including all events after start (exclusive)."""
        ...

    def at(self, time: Union[int, datetime, str]) -> "GraphView":
        """Create a view of the GraphView including all events at time."""
        ...

    def before(self, end: Union[int, datetime, str]) -> "GraphView":
        """Create a view of the GraphView including all events before end (exclusive)."""
        ...

    def bincode(self) -> bytes:
        """Get bincode encoded graph."""
        ...

    def count_edges(self) -> int:
        """Number of edges in the graph."""
        ...

    def count_nodes(self) -> int:
        """Number of nodes in the graph."""
        ...

    def count_temporal_edges(self) -> int:
        """Number of temporal edges in the graph."""
        ...

    def default_layer(self) -> "GraphView":
        """Return a view of GraphView containing only the default edge layer.

        :returns: The layered view
        :rtype: GraphView
        """
        ...

    @property
    def earliest_date_time(self) -> datetime:
        """DateTime of earliest activity in the graph."""
        ...

    @property
    def earliest_time(self) -> int:
        """Timestamp of earliest activity in the graph."""
        ...

    def edge(self, src: Union[str, int], dst: Union[str, int]) -> Optional["Edge"]:
        """Gets the edge with the specified source and destination nodes."""
        ...

    @property
    def edges(self) -> Iterator["Edge"]:
        """Gets all edges in the graph."""
        ...

    @property
    def end(self) -> Optional[int]:
        """Gets the latest time that this GraphView is valid."""
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        """Gets the latest datetime that this GraphView is valid."""
        ...

    def exclude_layer(self, name: str) -> "GraphView":
        """Return a view of GraphView containing all layers except the excluded name.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_layers(self, names: list[str]) -> "GraphView":
        """Return a view of GraphView containing all layers except the excluded names.

        Errors if any of the layers do not exist.
        """
        ...

    def exclude_nodes(self, nodes: list[Union[str, int]]) -> "GraphView":
        """Returns a subgraph given a set of nodes that are excluded from the subgraph."""
        ...

    def exclude_valid_layer(self, name: str) -> "GraphView":
        """Return a view of GraphView containing all layers except the excluded name.

        :param name: Layer name that is excluded for the new view
        :type name: str
        """
        ...

    def exclude_valid_layers(self, names: list[str]) -> "GraphView":
        """Return a view of GraphView containing all layers except the excluded names.

        :param names: List of layer names that are excluded for the new view
        :type names: list[str]
        """
        ...

    def expanding(self, step: Union[int, str]) -> "WindowSet":
        """Creates a WindowSet with the given step size using an expanding window."""
        ...

    def find_edges(self, properties_dict: dict[str, Any]) -> list["Edge"]:
        """Get the edges that match the properties name and value.

        :param properties_dict: The properties name and value
        :type properties_dict: dict
        """
        ...

    def find_nodes(self, properties_dict: dict[str, Any]) -> list["Node"]:
        """Get the nodes that match the properties name and value.

        :param properties_dict: The properties name and value
        :type properties_dict: dict
        """
        ...

    def get_all_node_types(self) -> list[str]:
        """Returns all the node types in the graph."""
        ...

    def has_edge(self, src: Union[str, int], dst: Union[str, int]) -> bool:
        """Returns true if the graph contains the specified edge."""
        ...

    def has_layer(self, name: str) -> bool:
        """Check if GraphView has the layer 'name'."""
        ...

    def has_node(self, id: Union[str, int]) -> bool:
        """Returns true if the graph contains the specified node."""
        ...

    def import_edge(
        self, edge: "Edge", force: bool = False
    ) -> Any:  # TODO: Result<EdgeView<Graph, Graph>, GraphError>
        """Import a single edge into the graph."""
        ...

    def import_edges(
        self, edges: list["Edge"], force: bool = False
    ) -> Any:  # TODO: Result<List(EdgeView<Graph, Graph>), GraphError>
        """Import multiple edges into the graph."""
        ...

    def import_node(
        self, node: "Node", force: bool = False
    ) -> Any:  # TODO: Result<NodeView<Graph, Graph>, GraphError>
        """Import a single node into the graph."""
        ...

    def import_nodes(
        self, nodes: list["Node"], force: bool = False
    ) -> Any:  # TODO: Result<List(NodeView<Graph, Graph>), GraphError>
        """Import multiple nodes into the graph."""
        ...

    def index(self) -> "GraphIndex":
        """Indexes all node and edge properties."""
        ...

    def largest_connected_component(self) -> "GraphView":
        """Gives the largest connected component of a graph."""
        ...

    @property
    def latest_date_time(self) -> datetime:
        """DateTime of latest activity in the graph."""
        ...

    @property
    def latest_time(self) -> int:
        """Timestamp of latest activity in the graph."""
        ...

    def layer(self, name: str) -> "GraphView":
        """Return a view of GraphView containing the layer 'name'.

        Errors if the layer does not exist.
        """
        ...

    def layers(self, names: list[str]) -> "GraphView":
        """Return a view of GraphView containing all layers names.

        Errors if any of the layers do not exist.
        """
        ...

    def load_edge_props_from_pandas(
        self,
        df: pd.DataFrame,
        src: str,
        dst: str,
        const_properties: Optional[list[str]] = None,
        shared_const_properties: Optional[dict[str, Any]] = None,
        layer: Optional[str] = None,
        layer_in_df: bool = True,
    ) -> Any:  # TODO: Result<(), GraphError>
        """Load edge properties from a Pandas DataFrame."""
        ...

    def load_edges_from_pandas(
        self,
        df: pd.DataFrame,
        src: str,
        dst: str,
        time: str,
        properties: Optional[list[str]] = None,
        const_properties: Optional[list[str]] = None,
        shared_const_properties: Optional[dict[str, Any]] = None,
        layer: Optional[str] = None,
        layer_in_df: bool = True,
    ) -> Any:  # TODO: Result<(), GraphError>
        """Load edges from a Pandas DataFrame into the graph."""
        ...

    @staticmethod
    def load_from_file(path: str, force: bool = False) -> "Graph":
        """Loads a graph from the given path."""
        ...

    @staticmethod
    def load_from_pandas(
        edge_df: pd.DataFrame,
        edge_src: str,
        edge_dst: str,
        edge_time: str,
        edge_properties: Optional[list[str]] = None,
        edge_const_properties: Optional[list[str]] = None,
        edge_shared_const_properties: Optional[dict[str, Any]] = None,
        edge_layer: Optional[str] = None,
        layer_in_df: bool = True,
        node_df: Optional[pd.DataFrame] = None,
        node_id: Optional[str] = None,
        node_time: Optional[str] = None,
        node_properties: Optional[list[str]] = None,
        node_const_properties: Optional[list[str]] = None,
        node_shared_const_properties: Optional[dict[str, Any]] = None,
        node_type: Optional[str] = None,
        node_type_in_df: bool = True,
    ) -> "GraphView":
        """Load a graph from a Pandas DataFrame."""
        ...

    def load_node_props_from_pandas(
        self,
        df: pd.DataFrame,
        id: str,
        const_properties: Optional[list[str]] = None,
        shared_const_properties: Optional[dict[str, Any]] = None,
    ) -> Any:
        """Load node properties from a Pandas DataFrame."""
        ...

    def load_nodes_from_pandas(
        self,
        df: pd.DataFrame,
        id: str,
        time: str,
        node_type: Optional[str] = None,
        node_type_in_df: bool = True,
        properties: Optional[list[str]] = None,
        const_properties: Optional[list[str]] = None,
        shared_const_properties: Optional[dict[str, Any]] = None,
    ) -> Any:
        """Load nodes from a Pandas DataFrame into the graph."""
        ...

    def materialize(self) -> "GraphView":
        """Returns a 'materialized' clone of the graph view - i.e. a new graph with a copy of the data seen within the view instead of just a mask over the original graph."""
        ...

    def node(self, id: Union[str, int]) -> Optional["Node"]:
        """Gets the node with the specified id."""
        ...

    @property
    def nodes(self) -> Iterator["Node"]:
        """Gets the nodes in the graph."""
        ...

    @property
    def properties(self) -> dict[str, Any]:
        """Get all graph properties."""
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> "WindowSet":
        """Creates a WindowSet with the given window size and optional step using a rolling window."""
        ...

    def save_to_file(self, path: str) -> None:
        """Saves the graph to the given path."""
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "GraphView":
        """Set the end of the window to the smaller of end and self.end()."""
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "GraphView":
        """Set the start of the window to the larger of start and self.start()."""
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "GraphView":
        """Shrink both the start and end of the window.

        Same as calling shrink_start followed by shrink_end but more efficient.
        """
        ...

    @property
    def start(self) -> Optional[int]:
        """Gets the start time for rolling and expanding windows for this GraphView."""
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        """Gets the earliest datetime that this GraphView is valid."""
        ...

    def subgraph(self, nodes: list[Union[str, int]]) -> "GraphView":
        """Returns a subgraph given a set of nodes."""
        ...

    def subgraph_node_types(self, node_types: list[str]) -> "GraphView":
        """Returns a subgraph filtered by node types given a set of node types."""
        ...

    def to_networkx(
        self,
        explode_edges: bool = False,
        include_node_properties: bool = True,
        include_edge_properties: bool = True,
        include_update_history: bool = True,
        include_property_history: bool = True,
    ) -> nx.MultiDiGraph:
        """Returns a graph with NetworkX."""
        ...

    def to_pyvis(
        self,
        explode_edges: bool = False,
        edge_color: str = "#000000",
        shape: Optional[str] = None,
        node_image: Optional[str] = None,
        edge_weight: Optional[str] = None,
        edge_label: Optional[str] = None,
        colour_nodes_by_type: bool = False,
        notebook: bool = False,
        **kwargs: Any,
    ) -> Any:  # TODO: PyVis type
        """Draw a graph with PyVis."""
        ...

    @property
    def unique_layers(self) -> list[str]:
        """Return all the layer ids in the graph."""
        ...

    def update_constant_properties(self, properties: dict[str, Any]) -> None:
        """Updates static properties to the graph."""
        ...

    def valid_layers(self, names: list[str]) -> "GraphView":
        """Return a view of GraphView containing all layers names.

        Any layers that do not exist are ignored.
        """
        ...

    def vectorise(
        self,
        embedding: Callable[[list[Any]], list[Any]],
        cache: Optional[str] = None,
        overwrite_cache: bool = False,
        graph_document: Optional[str] = None,
        node_document: Optional[str] = None,
        edge_document: Optional[str] = None,
        verbose: bool = False,
    ) -> "VectorisedGraph":
        """Create a VectorisedGraph from the current graph."""
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]],
        end: Optional[Union[int, datetime, str]],
    ) -> "GraphView":
        """Create a view of the GraphView including all events between start (inclusive) and end (exclusive)."""
        ...

    @property
    def window_size(self) -> Optional[int]:
        """Get the window size (difference between start and end) for this GraphView."""
        ...


class Graph(GraphView):
    """A temporal graph."""

    def persistent_graph(self) -> "PersistentGraph":
        """Get persistent graph."""
        ...

    ...


class PersistentGraph(GraphView):
    """A temporal graph that allows edges and nodes to be deleted."""

    def delete_edge(
        self,
        timestamp: int,
        src: Union[str, int],
        dst: Union[str, int],
        layer: Optional[str] = None,
    ):
        """Deletes an edge given the timestamp, src and dst nodes and layer (optional)"""
        ...

    def event_graph(self):
        """Get event graph"""
        ...
