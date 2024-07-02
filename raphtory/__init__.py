from datetime import datetime
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    Iterator,
    List,
    Optional,
    TypeVar,
    Union,
)

import networkx as nx
import pandas as pd

T = TypeVar("T", bound=Union["Graph", "GraphView", "Node", "Edge"])


# TODO: Double-check all of this, finish the rest of the classes
class VectorisedGraph:
    ...


class GraphIndex:
    ...


class WindowSet(Generic[T]):
    def __init__(
        self, obj: T, window: Union[int, str], step: Union[int, str, None] = None
    ):
        ...

    def __iter__(self) -> Iterator[T]:
        ...

    def __next__(self) -> T:
        ...

    def count(self) -> int:
        ...

    @property
    def start(self) -> int:
        ...

    @property
    def end(self) -> int:
        ...

    @property
    def step(self) -> int:
        ...

    @property
    def window(self) -> int:
        ...


class Node:
    def after(self, start: Union[int, datetime, str]) -> "Node":
        ...

    def at(self, time: Union[int, datetime, str]) -> "Node":
        ...

    def before(self, end: Union[int, datetime, str]) -> "Node":
        ...

    def default_layer(self) -> "Node":
        ...

    def degree(self) -> int:
        ...

    @property
    def earliest_date_time(self) -> datetime:
        ...

    @property
    def earliest_time(self) -> int:
        ...

    @property
    def edges(self) -> Iterator["Edge"]:
        ...

    @property
    def end(self) -> Optional[int]:
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        ...

    def exclude_layer(self, name: str) -> "Node":
        ...

    def exclude_layers(self, names: List[str]) -> "Node":
        ...

    def exclude_valid_layer(self, name: str) -> "Node":
        ...

    def exclude_valid_layers(self, names: List[str]) -> "Node":
        ...

    def expanding(self, step: Union[int, str]) -> WindowSet:
        ...

    def has_layer(self, name: str) -> bool:
        ...

    def history(self) -> List[int]:
        ...

    def history_date_time(self) -> List[datetime]:
        ...

    @property
    def id(self) -> Union[int, str]:
        ...

    def in_degree(self) -> int:
        ...

    @property
    def in_edges(self) -> Iterator["Edge"]:
        ...

    @property
    def in_neighbours(self) -> Iterator["Node"]:
        ...

    @property
    def latest_date_time(self) -> datetime:
        ...

    @property
    def latest_time(self) -> int:
        ...

    def layer(self, name: str) -> "Node":
        ...

    def layers(self, names: List[str]) -> "Node":
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def neighbours(self) -> Iterator["Node"]:
        ...

    @property
    def node_type(self) -> Optional[str]:
        ...

    def out_degree(self) -> int:
        ...

    @property
    def out_edges(self) -> Iterator["Edge"]:
        ...

    @property
    def out_neighbours(self) -> Iterator["Node"]:
        ...

    @property
    def properties(self) -> List[Any]:
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> WindowSet:
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "Node":
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "Node":
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "Node":
        ...

    @property
    def start(self) -> Optional[int]:
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        ...

    def valid_layers(self, names: List[str]) -> "Node":
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]],
        end: Optional[Union[int, datetime, str]],
    ) -> "Node":
        ...

    @property
    def window_size(self) -> Optional[int]:
        ...


class Edge:
    def after(self, start: Union[int, datetime, str]) -> "Edge":
        ...

    def at(self, time: Union[int, datetime, str]) -> "Edge":
        ...

    def before(self, end: Union[int, datetime, str]) -> "Edge":
        ...

    @property
    def date_time(self) -> datetime:
        ...

    def default_layer(self) -> "Edge":
        ...

    def deletions(self) -> List[int]:
        ...

    def deletions_data_time(self) -> List[datetime]:
        ...

    @property
    def dst(self) -> Node:
        ...

    @property
    def earliest_date_time(self) -> datetime:
        ...

    @property
    def earliest_time(self) -> int:
        ...

    @property
    def end(self) -> Optional[int]:
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        ...

    def exclude_layer(self, name: str) -> "Edge":
        ...

    def exclude_layers(self, names: List[str]) -> "Edge":
        ...

    def exclude_valid_layer(self, name: str) -> "Edge":
        ...

    def exclude_valid_layers(self, names: List[str]) -> "Edge":
        ...

    def expanding(self, step: Union[int, str]) -> WindowSet:
        ...

    def explode(self) -> List["Edge"]:
        ...

    def explode_layers(self) -> List["Edge"]:
        ...

    def has_layer(self, name: str) -> bool:
        ...

    def history(self) -> List[int]:
        ...

    def history_date_time(self) -> List[datetime]:
        ...

    @property
    def id(self) -> Union[int, str]:
        ...

    def is_deleted(self) -> bool:
        ...

    def is_self_loop(self) -> bool:
        ...

    def is_valid(self) -> bool:
        ...

    @property
    def latest_date_time(self) -> datetime:
        ...

    @property
    def latest_time(self) -> int:
        ...

    def layer(self, name: str) -> "Edge":
        ...

    @property
    def layer_name(self) -> str:
        ...

    @property
    def layer_names(self) -> List[str]:
        ...

    def layers(self, names: List[str]) -> "Edge":
        ...

    @property
    def nbr(self) -> Node:
        ...

    @property
    def properties(self) -> Dict[str, Any]:
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> WindowSet:
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "Edge":
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "Edge":
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "Edge":
        ...

    @property
    def src(self) -> Node:
        ...

    @property
    def start(self) -> Optional[int]:
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        ...

    @property
    def time(self) -> int:
        ...

    def valid_layers(self, names: List[str]) -> "Edge":
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]],
        end: Optional[Union[int, datetime, str]],
    ) -> "Edge":
        ...

    @property
    def window_size(self) -> Optional[int]:
        ...


class GraphView:
    def after(self, start: Union[int, datetime, str]) -> "GraphView":
        ...

    def at(self, time: Union[int, datetime, str]) -> "GraphView":
        ...

    def before(self, end: Union[int, datetime, str]) -> "GraphView":
        ...

    def bincode(self) -> bytes:
        ...

    def count_edges(self) -> int:
        ...

    def count_nodes(self) -> int:
        ...

    def count_temporal_edges(self) -> int:
        ...

    def default_layer(self) -> "GraphView":
        ...

    @property
    def earliest_date_time(self) -> datetime:
        ...

    @property
    def earliest_time(self) -> int:
        ...

    def edge(self, src: Union[str, int], dst: Union[str, int]) -> Optional[Edge]:
        ...

    @property
    def edges(self) -> Iterator[Edge]:
        ...

    @property
    def end(self) -> Optional[int]:
        ...

    @property
    def end_date_time(self) -> Optional[datetime]:
        ...

    def exclude_layer(self, name: str) -> "GraphView":
        ...

    def exclude_layers(self, names: List[str]) -> "GraphView":
        ...

    def exclude_nodes(self, nodes: Any) -> "GraphView":
        ...

    def exclude_valid_layer(self, name: str) -> "GraphView":
        ...

    def exclude_valid_layers(self, names: List[str]) -> "GraphView":
        ...

    def expanding(self, step: Union[int, str]) -> WindowSet:
        ...

    def find_edges(self, properties_dict: Dict[str, Any]) -> List[Edge]:
        ...

    def find_nodes(self, properties_dict: Dict[str, Any]) -> List[Node]:
        ...

    def get_all_node_types(self) -> List[str]:
        ...

    def has_edge(self, src: Union[str, int], dst: Union[str, int]) -> bool:
        ...

    def has_layer(self, name: str) -> bool:
        ...

    def has_node(self, id: Union[str, int]) -> bool:
        ...

    def index(self) -> GraphIndex:
        ...

    def largest_connected_component(self) -> "GraphView":
        ...

    @property
    def latest_date_time(self) -> datetime:
        ...

    @property
    def latest_time(self) -> int:
        ...

    def layer(self, name: str) -> "GraphView":
        ...

    def layers(self, names: List[str]) -> "GraphView":
        ...

    def materialize(self) -> "GraphView":
        ...

    def node(self, id: Union[str, int]) -> Optional[Node]:
        ...

    @property
    def nodes(self) -> Iterator[Node]:
        ...

    @property
    def properties(self) -> Dict[str, Any]:
        ...

    def rolling(
        self, window: Union[int, str], step: Optional[Union[int, str]] = None
    ) -> WindowSet:
        ...

    def shrink_end(self, end: Union[int, datetime, str]) -> "GraphView":
        ...

    def shrink_start(self, start: Union[int, datetime, str]) -> "GraphView":
        ...

    def shrink_window(
        self, start: Union[int, datetime, str], end: Union[int, datetime, str]
    ) -> "GraphView":
        ...

    @property
    def start(self) -> Optional[int]:
        ...

    @property
    def start_date_time(self) -> Optional[datetime]:
        ...

    def subgraph(self, nodes: Any) -> "GraphView":
        ...

    def subgraph_node_types(self, node_types: Any) -> "GraphView":
        ...

    def to_networkx(
        self,
        explode_edges: bool = False,
        include_node_properties: bool = True,
        include_edge_properties: bool = True,
        include_update_history: bool = True,
        include_property_history: bool = True,
    ) -> nx.MultiDiGraph:
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
    ) -> Any:
        ...

    @property
    def unique_layers(self) -> List[str]:
        ...

    def valid_layers(self, names: List[str]) -> "GraphView":
        ...

    def vectorise(
        self,
        embedding: Callable[[List[Any]], List[Any]],
        cache: Optional[str] = None,
        overwrite_cache: bool = False,
        graph_document: Optional[str] = None,
        node_document: Optional[str] = None,
        edge_document: Optional[str] = None,
        verbose: bool = False,
    ) -> VectorisedGraph:
        ...

    def window(
        self,
        start: Optional[Union[int, datetime, str]],
        end: Optional[Union[int, datetime, str]],
    ) -> "GraphView":
        ...

    @property
    def window_size(self) -> Optional[int]:
        ...


class Graph(GraphView):
    def add_constant_properties(self, properties: Dict[str, Any]) -> None:
        ...

    def add_edge(
        self,
        timestamp: Union[int, str, datetime],
        src: Union[str, int],
        dst: Union[str, int],
        properties: Optional[Dict[str, Any]] = None,
        layer: Optional[str] = None,
    ) -> None:
        ...

    def add_node(
        self,
        timestamp: Union[int, str, datetime],
        id: Union[str, int],
        properties: Optional[Dict[str, Any]] = None,
        node_type: Optional[str] = None,
    ) -> None:
        ...

    def add_property(
        self, timestamp: Union[int, str, datetime], properties: Dict[str, Any]
    ) -> None:
        ...

    def import_edge(self, edge: Edge, force: bool = False) -> Any:
        ...

    def import_edges(self, edges: List[Edge], force: bool = False) -> Any:
        ...

    def import_node(self, node: Node, force: bool = False) -> Any:
        ...

    def import_nodes(self, nodes: List[Node], force: bool = False) -> Any:
        ...

    def load_edge_props_from_pandas(
        self,
        df: pd.DataFrame,
        src: str,
        dst: str,
        const_properties: Optional[List[str]] = None,
        shared_const_properties: Optional[Dict[str, Any]] = None,
        layer: Optional[str] = None,
        layer_in_df: bool = True,
    ) -> Any:
        ...

    def load_edges_from_pandas(
        self,
        df: pd.DataFrame,
        src: str,
        dst: str,
        time: str,
        properties: Optional[List[str]] = None,
        const_properties: Optional[List[str]] = None,
        shared_const_properties: Optional[Dict[str, Any]] = None,
        layer: Optional[str] = None,
        layer_in_df: bool = True,
    ) -> Any:
        ...

    @staticmethod
    def load_from_file(path: str, force: bool = False) -> "Graph":
        ...

    @staticmethod
    def load_from_pandas(
        edge_df: pd.DataFrame,
        edge_src: str,
        edge_dst: str,
        edge_time: str,
        edge_properties: Optional[List[str]] = None,
        edge_const_properties: Optional[List[str]] = None,
        edge_shared_const_properties: Optional[Dict[str, Any]] = None,
        edge_layer: Optional[str] = None,
        layer_in_df: bool = True,
        node_df: Optional[pd.DataFrame] = None,
        node_id: Optional[str] = None,
        node_time: Optional[str] = None,
        node_properties: Optional[List[str]] = None,
        node_const_properties: Optional[List[str]] = None,
        node_shared_const_properties: Optional[Dict[str, Any]] = None,
        node_type: Optional[str] = None,
        node_type_in_df: bool = True,
    ) -> "Graph":
        ...

    def load_node_props_from_pandas(
        self,
        df: pd.DataFrame,
        id: str,
        const_properties: Optional[List[str]] = None,
        shared_const_properties: Optional[Dict[str, Any]] = None,
    ) -> Any:
        ...

    def load_nodes_from_pandas(
        self,
        df: pd.DataFrame,
        id: str,
        time: str,
        node_type: Optional[str] = None,
        node_type_in_df: bool = True,
        properties: Optional[List[str]] = None,
        const_properties: Optional[List[str]] = None,
        shared_const_properties: Optional[Dict[str, Any]] = None,
    ) -> Any:
        ...

    def persistent_graph(self) -> "Graph":
        ...

    def save_to_file(self, path: str) -> None:
        ...

    def update_constant_properties(self, properties: Dict[str, Any]) -> None:
        ...
