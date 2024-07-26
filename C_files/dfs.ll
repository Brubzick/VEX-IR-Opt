; ModuleID = 'dfs.c'
source_filename = "dfs.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

%struct.Graph = type { i32, [100 x %struct.Node*], [100 x i32] }
%struct.Node = type { i32, %struct.Node* }

@.str = private unnamed_addr constant [4 x i8] c"%d \00", align 1
@.str.1 = private unnamed_addr constant [24 x i8] c"Depth-First Traversal: \00", align 1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @initGraph(%struct.Graph* noundef %0, i32 noundef %1) #0 {
  %3 = alloca %struct.Graph*, align 8
  %4 = alloca i32, align 4
  %5 = alloca i32, align 4
  store %struct.Graph* %0, %struct.Graph** %3, align 8
  store i32 %1, i32* %4, align 4
  %6 = load i32, i32* %4, align 4
  %7 = load %struct.Graph*, %struct.Graph** %3, align 8
  %8 = getelementptr inbounds %struct.Graph, %struct.Graph* %7, i32 0, i32 0
  store i32 %6, i32* %8, align 8
  store i32 0, i32* %5, align 4
  br label %9

9:                                                ; preds = %24, %2
  %10 = load i32, i32* %5, align 4
  %11 = load i32, i32* %4, align 4
  %12 = icmp slt i32 %10, %11
  br i1 %12, label %13, label %27

13:                                               ; preds = %9
  %14 = load %struct.Graph*, %struct.Graph** %3, align 8
  %15 = getelementptr inbounds %struct.Graph, %struct.Graph* %14, i32 0, i32 1
  %16 = load i32, i32* %5, align 4
  %17 = sext i32 %16 to i64
  %18 = getelementptr inbounds [100 x %struct.Node*], [100 x %struct.Node*]* %15, i64 0, i64 %17
  store %struct.Node* null, %struct.Node** %18, align 8
  %19 = load %struct.Graph*, %struct.Graph** %3, align 8
  %20 = getelementptr inbounds %struct.Graph, %struct.Graph* %19, i32 0, i32 2
  %21 = load i32, i32* %5, align 4
  %22 = sext i32 %21 to i64
  %23 = getelementptr inbounds [100 x i32], [100 x i32]* %20, i64 0, i64 %22
  store i32 0, i32* %23, align 4
  br label %24

24:                                               ; preds = %13
  %25 = load i32, i32* %5, align 4
  %26 = add nsw i32 %25, 1
  store i32 %26, i32* %5, align 4
  br label %9, !llvm.loop !6

27:                                               ; preds = %9
  ret void
}

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @addEdge(%struct.Graph* noundef %0, i32 noundef %1, i32 noundef %2) #0 {
  %4 = alloca %struct.Graph*, align 8
  %5 = alloca i32, align 4
  %6 = alloca i32, align 4
  %7 = alloca %struct.Node*, align 8
  store %struct.Graph* %0, %struct.Graph** %4, align 8
  store i32 %1, i32* %5, align 4
  store i32 %2, i32* %6, align 4
  %8 = call noalias i8* @malloc(i64 noundef 16) #3
  %9 = bitcast i8* %8 to %struct.Node*
  store %struct.Node* %9, %struct.Node** %7, align 8
  %10 = load i32, i32* %6, align 4
  %11 = load %struct.Node*, %struct.Node** %7, align 8
  %12 = getelementptr inbounds %struct.Node, %struct.Node* %11, i32 0, i32 0
  store i32 %10, i32* %12, align 8
  %13 = load %struct.Graph*, %struct.Graph** %4, align 8
  %14 = getelementptr inbounds %struct.Graph, %struct.Graph* %13, i32 0, i32 1
  %15 = load i32, i32* %5, align 4
  %16 = sext i32 %15 to i64
  %17 = getelementptr inbounds [100 x %struct.Node*], [100 x %struct.Node*]* %14, i64 0, i64 %16
  %18 = load %struct.Node*, %struct.Node** %17, align 8
  %19 = load %struct.Node*, %struct.Node** %7, align 8
  %20 = getelementptr inbounds %struct.Node, %struct.Node* %19, i32 0, i32 1
  store %struct.Node* %18, %struct.Node** %20, align 8
  %21 = load %struct.Node*, %struct.Node** %7, align 8
  %22 = load %struct.Graph*, %struct.Graph** %4, align 8
  %23 = getelementptr inbounds %struct.Graph, %struct.Graph* %22, i32 0, i32 1
  %24 = load i32, i32* %5, align 4
  %25 = sext i32 %24 to i64
  %26 = getelementptr inbounds [100 x %struct.Node*], [100 x %struct.Node*]* %23, i64 0, i64 %25
  store %struct.Node* %21, %struct.Node** %26, align 8
  ret void
}

; Function Attrs: nounwind
declare noalias i8* @malloc(i64 noundef) #1

; Function Attrs: noinline nounwind optnone uwtable
define dso_local void @DFS(%struct.Graph* noundef %0, i32 noundef %1) #0 {
  %3 = alloca %struct.Graph*, align 8
  %4 = alloca i32, align 4
  %5 = alloca %struct.Node*, align 8
  store %struct.Graph* %0, %struct.Graph** %3, align 8
  store i32 %1, i32* %4, align 4
  %6 = load %struct.Graph*, %struct.Graph** %3, align 8
  %7 = getelementptr inbounds %struct.Graph, %struct.Graph* %6, i32 0, i32 2
  %8 = load i32, i32* %4, align 4
  %9 = sext i32 %8 to i64
  %10 = getelementptr inbounds [100 x i32], [100 x i32]* %7, i64 0, i64 %9
  store i32 1, i32* %10, align 4
  %11 = load i32, i32* %4, align 4
  %12 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([4 x i8], [4 x i8]* @.str, i64 0, i64 0), i32 noundef %11)
  %13 = load %struct.Graph*, %struct.Graph** %3, align 8
  %14 = getelementptr inbounds %struct.Graph, %struct.Graph* %13, i32 0, i32 1
  %15 = load i32, i32* %4, align 4
  %16 = sext i32 %15 to i64
  %17 = getelementptr inbounds [100 x %struct.Node*], [100 x %struct.Node*]* %14, i64 0, i64 %16
  %18 = load %struct.Node*, %struct.Node** %17, align 8
  store %struct.Node* %18, %struct.Node** %5, align 8
  br label %19

19:                                               ; preds = %37, %2
  %20 = load %struct.Node*, %struct.Node** %5, align 8
  %21 = icmp ne %struct.Node* %20, null
  br i1 %21, label %22, label %41

22:                                               ; preds = %19
  %23 = load %struct.Graph*, %struct.Graph** %3, align 8
  %24 = getelementptr inbounds %struct.Graph, %struct.Graph* %23, i32 0, i32 2
  %25 = load %struct.Node*, %struct.Node** %5, align 8
  %26 = getelementptr inbounds %struct.Node, %struct.Node* %25, i32 0, i32 0
  %27 = load i32, i32* %26, align 8
  %28 = sext i32 %27 to i64
  %29 = getelementptr inbounds [100 x i32], [100 x i32]* %24, i64 0, i64 %28
  %30 = load i32, i32* %29, align 4
  %31 = icmp ne i32 %30, 0
  br i1 %31, label %37, label %32

32:                                               ; preds = %22
  %33 = load %struct.Graph*, %struct.Graph** %3, align 8
  %34 = load %struct.Node*, %struct.Node** %5, align 8
  %35 = getelementptr inbounds %struct.Node, %struct.Node* %34, i32 0, i32 0
  %36 = load i32, i32* %35, align 8
  call void @DFS(%struct.Graph* noundef %33, i32 noundef %36)
  br label %37

37:                                               ; preds = %32, %22
  %38 = load %struct.Node*, %struct.Node** %5, align 8
  %39 = getelementptr inbounds %struct.Node, %struct.Node* %38, i32 0, i32 1
  %40 = load %struct.Node*, %struct.Node** %39, align 8
  store %struct.Node* %40, %struct.Node** %5, align 8
  br label %19, !llvm.loop !8

41:                                               ; preds = %19
  ret void
}

declare i32 @printf(i8* noundef, ...) #2

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca %struct.Graph, align 8
  store i32 0, i32* %1, align 4
  call void @initGraph(%struct.Graph* noundef %2, i32 noundef 6)
  call void @addEdge(%struct.Graph* noundef %2, i32 noundef 0, i32 noundef 1)
  call void @addEdge(%struct.Graph* noundef %2, i32 noundef 0, i32 noundef 2)
  call void @addEdge(%struct.Graph* noundef %2, i32 noundef 1, i32 noundef 3)
  call void @addEdge(%struct.Graph* noundef %2, i32 noundef 2, i32 noundef 4)
  call void @addEdge(%struct.Graph* noundef %2, i32 noundef 3, i32 noundef 5)
  %3 = call i32 (i8*, ...) @printf(i8* noundef getelementptr inbounds ([24 x i8], [24 x i8]* @.str.1, i64 0, i64 0))
  call void @DFS(%struct.Graph* noundef %2, i32 noundef 0)
  ret i32 0
}

attributes #0 = { noinline nounwind optnone uwtable "frame-pointer"="all" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nounwind "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { "frame-pointer"="all" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nounwind }

!llvm.module.flags = !{!0, !1, !2, !3, !4}
!llvm.ident = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 1}
!4 = !{i32 7, !"frame-pointer", i32 2}
!5 = !{!"Ubuntu clang version 14.0.0-1ubuntu1.1"}
!6 = distinct !{!6, !7}
!7 = !{!"llvm.loop.mustprogress"}
!8 = distinct !{!8, !7}
